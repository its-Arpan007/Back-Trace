from typing import Dict, Any
from app.engines.ai_engine.providers.base_provider import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):
    @property
    def provider_name(self) -> str:
        return "Gemini 1.5 Pro"

    async def generate_response(self, prompt: str, context: Dict[str, Any]) -> str:
        concept = context.get("target_concept", "DSA_ARRAYS_01")
        return f"[Gemini 1.5 Pro Cognitive Coach]: Based on your diagnostic analysis for '{concept}', remember that base addresses require multiplying the index by the element size in bytes."


gemini_provider = GeminiProvider()
