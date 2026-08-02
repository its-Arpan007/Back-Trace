import pytest
import uuid
from app.engines.diagnostic_engine.engine import DiagnosticEngine
from app.engines.mastery_engine.engine import MasteryEngine
from app.engines.recommendation_engine.engine import RecommendationEngine
from app.engines.analytics_engine.engine import AnalyticsEngine
from app.services.teacher_service import TeacherService
from app.services.admin_service import AdminService


@pytest.mark.asyncio
async def test_e2e_student_workflow():
    student_id = "11111111-1111-1111-1111-111111111111"
    
    # 1. Diagnostic Engine
    diag_engine = DiagnosticEngine()
    diag_res = await diag_engine.run_pipeline(
        student_id=student_id,
        question_id="q1_arrays_01",
        answer="0x1005",
        time_spent_seconds=45,
    )
    assert diag_res["pipeline_time_ms"] < 300.0
    assert diag_res["evaluation_result"]["is_correct"] is False

    # 2. Mastery Engine Update
    mastery_engine = MasteryEngine()
    mastery_res = await mastery_engine.process_learning_event(
        student_id=student_id,
        concept_code="DSA_ARRAYS_01",
        is_correct=False,
    )
    assert mastery_res["processing_time_ms"] < 100.0

    # 3. Adaptive Recommendation Generation
    rec_engine = RecommendationEngine()
    rec_res = await rec_engine.generate_recommendations(student_id, focus_concept_code="DSA_ARRAYS_01")
    assert rec_res["processing_time_ms"] < 300.0
    assert len(rec_res["recommendations"]) >= 2

    # 4. Analytics Engine Aggregation
    analytics_engine = AnalyticsEngine()
    analytics_res = await analytics_engine.generate_student_analytics(student_id)
    assert analytics_res["processing_time_ms"] < 500.0


@pytest.mark.asyncio
async def test_e2e_teacher_workflow():
    teacher_id = uuid.uuid4()
    teacher_service = TeacherService(None)
    
    classes = await teacher_service.get_teacher_classes(teacher_id)
    assert len(classes) > 0

    analytics = await teacher_service.get_class_analytics("c_dsa_101")
    assert analytics.average_mastery > 0.0

    interventions = await teacher_service.get_intervention_candidates(teacher_id)
    assert len(interventions) > 0


@pytest.mark.asyncio
async def test_e2e_admin_workflow():
    admin_service = AdminService(None)
    
    dashboard = await admin_service.get_dashboard_summary()
    assert dashboard.system_status == "healthy"

    health = await admin_service.get_system_health()
    assert health.api_status == "operational"

    backup = await admin_service.trigger_backup()
    assert backup["status"] == "completed"
