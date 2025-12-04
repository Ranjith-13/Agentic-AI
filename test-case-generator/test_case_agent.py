import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

class TestCaseGeneratorAgent:
    """
    Advanced agent that:
    - Reads Python code
    - Extracts functions, parameters, behaviors
    - Generates test plan + pytest file
    """

    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def generate_test_cases(self, code: str) -> dict:

        system_prompt = """
You are a senior Python QA engineer.

STRICT RULES (VIOLATION → INVALID):
- Output ONLY valid JSON.
- Do NOT wrap JSON in ```json``` or any code block.
- No explanation outside JSON.
- No comments.
- JSON must contain exactly these fields:

{
 "test_plan": "markdown content",
 "test_file": "pytest file content"
}

"""

        user_prompt = (
            "Read the following Python code and generate a test plan and pytest file.\n\n"
            f"CODE:\n```python\n{code}\n```"
        )

        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
            max_tokens=4096
        )

        raw = response.choices[0].message.content

        # Validate JSON
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            raise ValueError("\n❌ LLM returned invalid JSON:\n\n" + raw)
