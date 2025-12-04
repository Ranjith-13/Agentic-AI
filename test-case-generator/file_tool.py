from pathlib import Path

def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    return p.read_text()

def save_text(content: str, output: str):
    Path(output).write_text(content)
    print(f"Saved → {output}")
