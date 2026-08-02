import logging
from typing import Dict, Type, Optional, Any, List
from app.domain.interfaces.engine import IEngine

logger = logging.getLogger("backtrace.engine_registry")


class EngineRegistry:
    """Central Engine Registry managing engine lifecycle, resolution, lazy loading, and health checks."""

    def __init__(self) -> None:
        self._engine_classes: Dict[str, Type[IEngine]] = {}
        self._instances: Dict[str, IEngine] = {}

    def register(self, name: str, engine_cls: Type[IEngine]) -> None:
        self._engine_classes[name.lower()] = engine_cls
        logger.info(f"Registered engine class: '{name}'")

    def get(self, name: str) -> Optional[IEngine]:
        key = name.lower()
        if key in self._instances:
            return self._instances[key]

        if key in self._engine_classes:
            cls = self._engine_classes[key]
            instance = cls()
            self._instances[key] = instance
            logger.info(f"Lazy-loaded engine instance for '{name}'")
            return instance

        logger.warning(f"Engine '{name}' not found in registry")
        return None

    async def get_health_summary(self) -> Dict[str, Any]:
        report: Dict[str, Any] = {}
        all_healthy = True

        for name in list(self._engine_classes.keys()):
            engine = self.get(name)
            if engine:
                healthy = await engine.health_check()
                ready = await getattr(engine, "readiness", lambda: True)() if callable(getattr(engine, "readiness", None)) else True
                version = getattr(engine, "version", "1.0.0")
                status = getattr(engine, "status", "healthy" if healthy else "degraded")
                dependencies = getattr(engine, "dependencies", [])

                report[name] = {
                    "name": getattr(engine, "name", name),
                    "version": version,
                    "status": status,
                    "healthy": healthy,
                    "ready": ready,
                    "dependencies": dependencies,
                }
                if not (healthy and ready):
                    all_healthy = False

        return {
            "status": "healthy" if all_healthy else "degraded",
            "total_engines": len(report),
            "engines": report,
        }


engine_registry = EngineRegistry()
