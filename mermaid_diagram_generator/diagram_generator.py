class DiagramGenerator:
    BASE_PROMPT = """
You are an expert software architect.
Convert the given Python code into a clean, accurate Mermaid diagram.
Choose the best diagram type (flowchart, class diagram, or sequence diagram).
Return ONLY the Mermaid diagram.
"""

    def build_prompt(self, code: str) -> str:
        return f"{self.BASE_PROMPT}\n\n```python\n{code}\n```"
