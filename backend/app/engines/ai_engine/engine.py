import time
from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.ai_engine.context_builder import context_builder
from app.engines.ai_engine.prompt_builder import prompt_builder
from app.engines.ai_engine.safety_layer import safety_layer
from app.engines.ai_engine.response_validator import response_validator
from app.engines.ai_engine.providers.gemini_provider import gemini_provider
from app.engines.ai_engine.providers.openai_provider import openai_provider
from app.engines.ai_engine.providers.anthropic_provider import anthropic_provider
from app.engines.ai_engine.providers.ollama_provider import ollama_provider


class AIEngine(IEngine):
    """Production AI Enhancement Pipeline Orchestrator."""

    def __init__(self):
        self.providers = {
            "gemini": gemini_provider,
            "openai": openai_provider,
            "anthropic": anthropic_provider,
            "ollama": ollama_provider,
        }

    @property
    def name(self) -> str:
        return "AI Enhancement Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return ["Diagnostic Engine", "Student Learning Model", "Adaptive Recommendation Engine"]

    async def generate_enhanced_response(
        self,
        user_id: str,
        message: str,
        concept_code: str = "DSA_ARRAYS_01",
        provider_name: str = "gemini",
    ) -> Dict[str, Any]:
        start_time = time.time()

        # 1. Safety & Moderation
        safe_check = safety_layer.sanitize_and_validate(message)
        if not safe_check["is_safe"]:
            return {
                "reply": "Request rejected due to safety guidelines.",
                "grounded_in_diagnosis": True,
                "suggested_actions": ["Ask a question about your concept diagnosis."],
                "processing_time_ms": round((time.time() - start_time) * 1000, 2),
            }

        # 2. Context Building (<100ms)
        ctx = context_builder.build_context(user_id, concept_code)

        # 3. Prompt Building (<50ms)
        prompt = prompt_builder.build_student_coach_prompt(safe_check["sanitized_text"], ctx)

        # 4. LLM Provider Execution
        provider = self.providers.get(provider_name.lower(), gemini_provider)
        raw_response = await provider.generate_response(prompt, ctx)

        # 5. Deterministic Grounding & Response Validation
        valid_res = response_validator.validate_grounding(raw_response, ctx)

        proc_time = (time.time() - start_time) * 1000

        return {
            "reply": valid_res["validated_output"],
            "grounded_in_diagnosis": valid_res["is_grounded"],
            "context_used": ctx,
            "suggested_actions": [
                "Launch Interactive Visualizer for DSA_ARRAYS_01",
                "Try a 3-question targeted practice session",
            ],
            "processing_time_ms": round(proc_time, 2),
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.generate_enhanced_response(
            user_id=input_data.get("user_id", "student_1"),
            message=input_data.get("message", "How do I calculate array memory offset?"),
            concept_code=input_data.get("concept_code", "DSA_ARRAYS_01"),
            provider_name=input_data.get("provider", "gemini"),
        )

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True


ai_engine = AIEngine()
