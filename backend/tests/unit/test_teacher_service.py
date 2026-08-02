import pytest
import uuid
from app.services.teacher_service import TeacherService
from app.schemas.teacher import AssessmentBuildRequest, AssignmentCreateRequest


@pytest.mark.asyncio
async def test_teacher_service_classes():
    service = TeacherService(None)
    classes = await service.get_teacher_classes(uuid.uuid4())
    assert len(classes) == 2
    assert classes[0].total_students == 32


@pytest.mark.asyncio
async def test_build_assessment_from_knowledge_graph():
    service = TeacherService(None)
    req = AssessmentBuildRequest(title="Array Quiz", target_concept_codes=["DSA_ARRAYS_01"], question_count=5)
    res = await service.build_assessment(req)
    assert res["title"] == "Array Quiz"
    assert len(res["questions"]) > 0
