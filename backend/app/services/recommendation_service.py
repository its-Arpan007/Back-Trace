import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recommendation import RecommendationModel
from app.repositories.recommendation_repository import RecommendationRepository
from app.engines.recommendation_engine.engine import RecommendationEngine
from app.engines.recommendation_engine.plan_engine import plan_engine
from app.engines.recommendation_engine.revision_engine import revision_engine
from app.engines.recommendation_engine.resource_matcher import resource_matcher
from app.engines.recommendation_engine.question_recommender import question_recommender
from app.engines.recommendation_engine.goal_engine import goal_engine
from app.engines.recommendation_engine.path_engine import path_engine
from app.schemas.recommendation import (
    RecommendationDTO,
    LearningPlanDTO,
    DailyLearningPlanDTO,
    WeeklyLearningPlanDTO,
    RevisionScheduleDTO,
    ResourceRecommendationDTO,
    QuestionRecommendationDTO,
    GoalRecommendationDTO,
    RecommendationFeedbackRequest,
    GenerateRecommendationsRequest,
)


class RecommendationService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = RecommendationRepository(db)
        self.engine = RecommendationEngine()

    async def get_student_recommendations(self, student_id: uuid.UUID) -> List[RecommendationDTO]:
        recs = await self.repo.get_student_recommendations(student_id)
        if not recs:
            # Generate default fallback recommendations
            gen_res = await self.engine.generate_recommendations(str(student_id))
            for r in gen_res["recommendations"]:
                await self.repo.create_recommendation({
                    "student_id": student_id,
                    "recommendation_type": r["recommendation_type"],
                    "title": r["title"],
                    "description": r["description"],
                    "target_concept_code": r["target_concept_code"],
                    "priority_score": r["priority_score"],
                    "urgency_level": r["urgency_level"],
                    "expected_improvement_delta": r["expected_improvement_delta"],
                    "est_duration_minutes": r["est_duration_minutes"],
                    "reasoning_explanation": r["reasoning_explanation"],
                    "evidence_json": r["evidence"],
                })
            recs = await self.repo.get_student_recommendations(student_id)

        return [
            RecommendationDTO(
                recommendation_id=str(r.id),
                student_id=str(r.student_id),
                recommendation_type=r.recommendation_type,
                title=r.title,
                description=r.description,
                target_concept_code=r.target_concept_code,
                priority_score=r.priority_score,
                urgency_level=r.urgency_level,
                expected_improvement_delta=r.expected_improvement_delta,
                est_duration_minutes=r.est_duration_minutes,
                reasoning_explanation=r.reasoning_explanation,
                evidence=r.evidence_json or [],
                is_completed=r.is_completed,
            )
            for r in recs
        ]

    async def get_todays_plan(self, student_id: uuid.UUID) -> LearningPlanDTO:
        recs = await self.get_student_recommendations(student_id)
        plan_dict = plan_engine.generate_todays_plan(str(student_id), ["DSA_ARRAYS_01"], [r.model_dump() for r in recs])
        return LearningPlanDTO(
            student_id=str(student_id),
            plan_type="today",
            plan_title=plan_dict["plan_title"],
            concepts_sequence=plan_dict["concepts_sequence"],
            estimated_duration_minutes=plan_dict["estimated_duration_minutes"],
            expected_outcome=plan_dict["expected_outcome"],
            recommendations=recs,
        )

    async def get_weekly_plan(self, student_id: uuid.UUID) -> WeeklyLearningPlanDTO:
        now = datetime.now(timezone.utc)
        return WeeklyLearningPlanDTO(
            student_id=str(student_id),
            week_start_date=now,
            daily_targets={
                "Monday": ["DSA_ARRAYS_01 - Memory Layout"],
                "Tuesday": ["DSA_ARRAYS_01 - Stride Calculation"],
                "Wednesday": ["DSA_TREES_01 - BST Traversal Revision"],
                "Thursday": ["DSA_HASH_01 - Collision Resolution"],
                "Friday": ["DSA_ARRAYS_01 & TREES Practice Set"],
            },
            target_mastery_avg=0.88,
        )

    async def get_revision_schedule(self, student_id: uuid.UUID) -> List[RevisionScheduleDTO]:
        revs = revision_engine.schedule_revisions(str(student_id), [{"concept_code": "DSA_ARRAYS_01", "knowledge_decay": 0.22}])
        return [
            RevisionScheduleDTO(
                student_id=str(student_id),
                concept_code=r["concept_code"],
                scheduled_date=r["scheduled_date"],
                revision_reason=r["revision_reason"],
            )
            for r in revs
        ]

    async def get_recommended_resources(self, student_id: uuid.UUID) -> List[ResourceRecommendationDTO]:
        res_list = resource_matcher.match_resources("DSA_ARRAYS_01")
        return [
            ResourceRecommendationDTO(
                resource_id=r["resource_id"],
                resource_type=r["resource_type"],
                title=r["title"],
                url=r["url"],
                difficulty=r["difficulty"],
                est_minutes=r["est_minutes"],
                match_score=r["match_score"],
            )
            for r in res_list
        ]

    async def get_recommended_questions(self, student_id: uuid.UUID) -> List[QuestionRecommendationDTO]:
        q_list = question_recommender.recommend_questions("DSA_ARRAYS_01", count=3)
        return [
            QuestionRecommendationDTO(
                question_id=q["question_id"],
                concept_code=q["concept_code"],
                question_statement=q["question_statement"],
                difficulty=q["difficulty"],
                bloom_level=q["bloom_level"],
                recommendation_reason=q["recommendation_reason"],
            )
            for q in q_list
        ]

    async def get_recommended_goals(self, student_id: uuid.UUID) -> List[GoalRecommendationDTO]:
        g_list = goal_engine.generate_goals(str(student_id))
        return [
            GoalRecommendationDTO(
                goal_title=g["goal_title"],
                target_mastery=g["target_mastery"],
                reasoning=g["reasoning"],
            )
            for g in g_list
        ]

    async def log_feedback(self, req: RecommendationFeedbackRequest) -> Dict[str, Any]:
        await self.repo.log_feedback(
            student_id=uuid.UUID(req.student_id),
            rec_id=uuid.UUID(req.recommendation_id),
            rating=req.rating_score,
            text=req.feedback_text or "",
            action=req.action_taken,
        )
        return {"status": "success", "message": "Feedback recorded"}

    async def generate_fresh_recommendations(self, req: GenerateRecommendationsRequest) -> Dict[str, Any]:
        focus = req.focus_concept_code or "DSA_ARRAYS_01"
        return await self.engine.generate_recommendations(req.student_id, focus_concept_code=focus)
