from typing import Dict, Any
from app.engines.ai_engine.providers.base_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    @property
    def provider_name(self) -> str:
        return "OpenAI GPT-4o"

    async def generate_response(self, prompt: str, context: Dict[str, Any]) -> str:
        return f"[OpenAI GPT-4o Assistant]: Let's break down your prerequisite gap in memory layout calculation step by step."


openai_provider = OpenAIProvider()
