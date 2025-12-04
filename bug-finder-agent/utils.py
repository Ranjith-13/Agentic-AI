# utils.py
from pathlib import Path

def save_output(content: str, out_file: str = "analysis.md"):
    Path(out_file).write_text(content, encoding="utf-8")
    print(f"Saved output to {out_file}")
