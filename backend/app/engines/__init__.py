from app.engines.rule_engine.engine import RuleEngine
from app.engines.ai_engine.engine import AIEngine
from app.engines.diagnostic_engine.engine import DiagnosticEngine
from app.engines.knowledge_graph_engine.engine import KnowledgeGraphEngine
from app.engines.mastery_engine.engine import MasteryEngine
from app.engines.bayesian_engine.engine import BayesianEngine
from app.engines.recommendation_engine.engine import RecommendationEngine
from app.engines.analytics_engine.engine import AnalyticsEngine
from app.engines.decision_engine.engine import DecisionEngine
from app.engines.engine_registry import engine_registry

# Register all platform engines in Central Registry
engine_registry.register("rule", RuleEngine)
engine_registry.register("ai", AIEngine)
engine_registry.register("diagnostic", DiagnosticEngine)
engine_registry.register("knowledge_graph", KnowledgeGraphEngine)
engine_registry.register("mastery", MasteryEngine)
engine_registry.register("bayesian", BayesianEngine)
engine_registry.register("recommendation", RecommendationEngine)
engine_registry.register("analytics", AnalyticsEngine)
engine_registry.register("decision", DecisionEngine)

__all__ = [
    "RuleEngine",
    "AIEngine",
    "DiagnosticEngine",
    "KnowledgeGraphEngine",
    "MasteryEngine",
    "BayesianEngine",
    "RecommendationEngine",
    "AnalyticsEngine",
    "DecisionEngine",
    "engine_registry",
]
