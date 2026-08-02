from fastapi import APIRouter
from app.api.v1.endpoints import (
    health,
    auth,
    profile,
    subjects,
    chapters,
    topics,
    concepts,
    graph,
    knowledge_graph,
    questions,
    diagnostics,
    mastery,
    recommendations,
    analytics,
    teacher,
    admin,
    ai,
)

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(profile.router)
api_router.include_router(subjects.router)
api_router.include_router(chapters.router)
api_router.include_router(topics.router)
api_router.include_router(concepts.router)
api_router.include_router(graph.router)
api_router.include_router(questions.router)
api_router.include_router(knowledge_graph.router)
api_router.include_router(diagnostics.router)
api_router.include_router(mastery.router)
api_router.include_router(recommendations.router)
api_router.include_router(analytics.router)
api_router.include_router(teacher.router)
api_router.include_router(admin.router)
api_router.include_router(ai.router)
