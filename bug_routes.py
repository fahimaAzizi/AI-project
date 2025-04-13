import openai
import pylint.lint
import subprocess
from fastapi import FastAPI, Form, Depends, HTTPException, Request
from fastapi.security import OAuth2AuthorizationCodeBearer
from authlib.integrations.starlette_client import OAuth
from pathlib import Path
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
import os

# Initialize FastAPI app
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# OpenAI API Key (Ensure to set this securely, e.g., using environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Temporary file path
TEMP_FILE = Path("temp.py")

# OAuth2 Configuration (Google/GitHub Login)
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

# OAuth2 Authorization
@app.get("/login/{provider}")
async def login(request: Request, provider: str):
    if provider not in ["google", "github"]:
        raise HTTPException(status_code=400, detail="Unsupported provider")
    redirect_uri = request.url_for("auth_callback", provider=provider)
    return await oauth.create_client(provider).authorize_redirect(request, redirect_uri)

@app.get("/auth/{provider}")
async def auth_callback(request: Request, provider: str):
    token = await oauth.create_client(provider).authorize_access_token(request)
    user_info = await oauth.create_client(provider).parse_id_token(request, token) if provider == "google" else token
    return {"message": "Login successful", "user": user_info}

# Root endpoint (returns "Hello, FastAPI!" when accessed)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Function to analyze code with Pylint
def analyze_code(code_snippet):
    TEMP_FILE.write_text(code_snippet)
    pylint_opts = [str(TEMP_FILE)]
    results = pylint.lint.Run(pylint_opts, do_exit=False)
    return results.linter.reporter.data

# Function to check security vulnerabilities with Bandit
def check_security(code_snippet):
    TEMP_FILE.write_text(code_snippet)
    result = subprocess.run(["bandit", "-r", str(TEMP_FILE)], capture_output=True, text=True)
    return result.stdout

# Function to detect bugs using GPT-4
def detect_bugs(code_snippet):
    prompt = f"Find bugs in the following Python code and suggest fixes:\n\n{code_snippet}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert code reviewer."},
                  {"role": "user", "content": prompt}]
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
