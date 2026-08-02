from typing import Dict, Any
from app.engines.engine_registry import engine_registry


class AnalyticsPipeline:
    async def execute(self, student_id: str) -> Dict[str, Any]:
        analytics_engine = engine_registry.get("analytics")
        return await analytics_engine.process({"student_id": student_id})


analytics_pipeline = AnalyticsPipeline()
