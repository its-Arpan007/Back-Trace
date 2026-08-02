from typing import Dict, Any
from app.engines.ai_engine.engine import ai_engine
from app.schemas.ai import (
    AIChatRequest,
    AIChatResponse,
    AIExplainRequest,
    AIStudyPlanRequest,
    AIGenerateQuestionRequest,
    AIReflectionRequest,
)


class AIService:
    async def chat(self, req: AIChatRequest) -> AIChatResponse:
        res = await ai_engine.generate_enhanced_response(
            user_id=req.user_id,
            message=req.message,
            concept_code=req.concept_code or "DSA_ARRAYS_01",
            provider_name=req.provider,
        )
        return AIChatResponse(
            reply=res["reply"],
            grounded_in_diagnosis=res["grounded_in_diagnosis"],
            context_used=res["context_used"],
            suggested_actions=res["suggested_actions"],
            processing_time_ms=res["processing_time_ms"],
        )

    async def explain(self, req: AIExplainRequest) -> Dict[str, Any]:
        return {
            "concept_code": req.concept_code,
            "explanation_type": req.explanation_type,
            "analogy": "Think of memory addresses like postal mailboxes arranged in a linear row. Each box holds 4 bytes of data.",
            "mnemonic": "Address = Base + (Index * Byte Size)",
        }

    async def generate_study_plan(self, req: AIStudyPlanRequest) -> Dict[str, Any]:
        return {
            "student_id": req.student_id,
            "target_date": req.target_date,
            "daily_plan": [
                {"day": 1, "task": "Review Memory Stride visualizer (20 mins)"},
                {"day": 2, "task": "Practice 5 Array Offset questions (25 mins)"},
            ],
        }

    async def generate_question(self, req: AIGenerateQuestionRequest) -> Dict[str, Any]:
        return {
            "concept_code": req.concept_code,
            "bloom_level": req.bloom_level,
            "difficulty": req.difficulty,
            "question_text": "Given base address 0x2000 and 4-byte integers, what is the address of element at index 3?",
            "expected_answer": "0x200C",
            "validation_status": "passed_validator",
        }
