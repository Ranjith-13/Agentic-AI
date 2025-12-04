# agent_llm.py
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

class AgentLLM:
    """Base class for Azure OpenAI LLM access"""

    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def generate(self, system_prompt: str, user_prompt: str,
                 max_tokens: int = 1200, temperature: float = 0.2):

        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )

        return response.choices[0].message.content
