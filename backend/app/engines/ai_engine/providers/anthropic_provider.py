from typing import Dict, Any
from app.engines.ai_engine.providers.base_provider import BaseLLMProvider


class AnthropicProvider(BaseLLMProvider):
    @property
    def provider_name(self) -> str:
        return "Anthropic Claude 3.5 Sonnet"

    async def generate_response(self, prompt: str, context: Dict[str, Any]) -> str:
        return f"[Claude 3.5 Sonnet Assistant]: Imagine memory addresses like apartment numbers where each apartment takes 4 door slots."


anthropic_provider = AnthropicProvider()
