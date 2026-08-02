from typing import Dict, Any
from app.engines.ai_engine.providers.base_provider import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    @property
    def provider_name(self) -> str:
        return "Ollama Local (Offline Mode)"

    async def generate_response(self, prompt: str, context: Dict[str, Any]) -> str:
        return f"[Ollama Offline Assistant]: Offline learning mode active. Address = Base + (Index * Stride)."


ollama_provider = OllamaProvider()
