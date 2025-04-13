import subprocess
from pathlib import Path

def check_security(code_snippet: str, file_path: Path) -> str:
    file_path.write_text(code_snippet)
    result = subprocess.run(["bandit", "-r", str(file_path)], capture_output=True, text=True)
    return result.stdout
