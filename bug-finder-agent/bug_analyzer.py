# bug_analyzer.py
from agent_llm import AgentLLM

class BugAnalyzerAgent(AgentLLM):
    """Agent that detects bugs and suggests fixes in Python code."""

    def analyze(self, code: str) -> str:
        system_prompt = (
            "You are a senior Python code auditor.\n"
            "Your duties:\n"
            "1. Identify bugs and vulnerabilities.\n"
            "2. Explain the issue briefly.\n"
            "3. Provide corrected code.\n"
            "4. Mention line numbers.\n"
            "Return a clean markdown report."
        )

        user_prompt = f"Analyze the following Python code:\n```python\n{code}\n```"

        return self.generate(system_prompt, user_prompt)
