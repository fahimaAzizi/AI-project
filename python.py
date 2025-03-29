import openai
import pylint.lint
import subprocess
from fastapi import FastAPI, Form
from pathlib import Path

# Initialize FastAPI app
app = FastAPI()

# OpenAI API Key (Ensure to set this securely, e.g., using environment variables)
openai.api_key = "your_openai_api_key"

# Temporary file path
TEMP_FILE = Path("temp.py")

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
    try:
        bug_report = detect_bugs(code)
        pylint_report = analyze_code(code)
        security_report = check_security(code)
    except Exception as e:
        return {"error": str(e)}
    
    return {
        "bug_report": bug_report,
        "pylint_report": pylint_report,
        "security_report": security_report
    }
