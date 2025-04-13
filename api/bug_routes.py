import openai
import tempfile
import subprocess
import os
import io

from fastapi import FastAPI, Form, Depends, HTTPException, Request
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from pylint.lint import Run
from pylint.reporters.text import TextReporter

# Initialize FastAPI app
app = FastAPI()

# CORS for frontend integration (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with specific domain(s) in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session middleware for OAuth
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# OAuth2 Configuration (Google and GitHub)
oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params={"scope": "email profile"},
    access_token_url="https://oauth2.googleapis.com/token",
    client_kwargs={'scope': 'openid email profile'}
)

oauth.register(
    name='github',
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    authorize_url="https://github.com/login/oauth/authorize",
    access_token_url="https://github.com/login/oauth/access_token",
    client_kwargs={'scope': 'user:email'}
)

# Login endpoint
@app.get("/login/{provider}")
async def login(request: Request, provider: str):
    if provider not in ["google", "github"]:
        raise HTTPException(status_code=400, detail="Unsupported provider")
    redirect_uri = request.url_for("auth_callback", provider=provider)
    return await oauth.create_client(provider).authorize_redirect(request, redirect_uri)

# OAuth callback
@app.get("/auth/{provider}")
async def auth_callback(request: Request, provider: str):
    client = oauth.create_client(provider)
    token = await client.authorize_access_token(request)
    
    if provider == "google":
        user_info = await client.parse_id_token(request, token)
    elif provider == "github":
        user_info_response = await client.get("user", token=token)
        user_info = user_info_response.json()
    else:
        raise HTTPException(status_code=400, detail="Unsupported provider")
    
    return {"message": "Login successful", "user": user_info}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Analyze code with Pylint
def analyze_code(code_snippet):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp:
        temp.write(code_snippet.encode())
        temp.flush()
        output = io.StringIO()
        reporter = TextReporter(output)
        Run([temp.name], reporter=reporter, do_exit=False)
        return output.getvalue()

# Check security with Bandit
def check_security(code_snippet):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp:
        temp.write(code_snippet.encode())
        temp.flush()
        result = subprocess.run(["bandit", "-r", temp.name], capture_output=True, text=True)
        return result.stdout

# Detect bugs using GPT
def detect_bugs(code_snippet):
    prompt = f"Find bugs in the following Python code and suggest fixes:\n\n{code_snippet}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

# API endpoint to detect bugs
@app.post("/detect_bugs/")
def detect_bugs_endpoint(code: str = Form(...)):
    message = ""
    if "youtube" in code.lower():
        message += "Yes, there is YouTube.\n"
    if "facebook" in code.lower():
        message += "Yes, there is Facebook.\n"

    try:
        bug_report = detect_bugs(code)
        pylint_report = analyze_code(code)
        security_report = check_security(code)
    except Exception as e:
        return {"error": str(e)}

    return {
        "message": message.strip(),
        "bug_report": bug_report,
        "pylint_report": pylint_report,
        "security_report": security_report
    }
