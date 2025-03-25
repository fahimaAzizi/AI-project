import openai
import pylint.lint
import subprocess
from fastapi import FastAPI, Form

# Initialize FastAPI app
app = FastAPI()

# OpenAI API Key (Replace with your key)
openai.api_key = "your_openai_api_key"

# Function to analyze code with Pylint
def analyze_code(code_snippet):
    with open("temp.py", "w") as f:
        f.write(code_snippet)
    pylint_opts = ["temp.py"]
    results = pylint.lint.Run(pylint_opts, do_exit=False)
    return results.linter.reporter.data

# Function to check security vulnerabilities with Bandit



    
   


