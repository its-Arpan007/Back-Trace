from typing import Dict, Any, Callable, Coroutine

HealthCheckFunc = Callable[[], Coroutine[Any, Any, bool]]


class SystemHealthMonitor:
    def __init__(self) -> None:
        self._checks: Dict[str, HealthCheckFunc] = {}

    def register_check(self, name: str, func: HealthCheckFunc) -> None:
        self._checks[name] = func

    async def run_all_checks(self) -> Dict[str, Any]:
        results = {}
        all_healthy = True

        for name, func in self._checks.items():
            try:
                is_healthy = await func()
                results[name] = "healthy" if is_healthy else "unhealthy"
                if not is_healthy:
                    all_healthy = False
            except Exception:
                results[name] = "error"
                all_healthy = False

        return {
            "status": "healthy" if all_healthy else "degraded",
            "services": results,
        }


health_monitor = SystemHealthMonitor()
