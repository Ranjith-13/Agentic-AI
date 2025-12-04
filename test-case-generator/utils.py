# utils.py

def sanitize_filename(name: str) -> str:
    return name.replace(" ", "_").lower()
