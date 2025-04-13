import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

def detect_bugs(code_snippet: str) -> str:
    prompt = f"Find bugs in the following Python code and suggest fixes:\n\n{code_snippet}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]
