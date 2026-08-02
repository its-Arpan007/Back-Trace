import time
import logging
from contextlib import asynccontextmanager
from typing import Dict, Any

logger = logging.getLogger("backtrace.metrics")


class PerformanceTimer:
    def __init__(self, operation_name: str) -> None:
        self.operation_name = operation_name
        self.start_time: float = 0.0

    def __enter__(self) -> "PerformanceTimer":
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        elapsed = (time.time() - self.start_time) * 1000
        logger.info(f"[PERF] {self.operation_name} executed in {elapsed:.2f}ms")


class MetricsCollector:
    def __init__(self) -> None:
        self._api_counts: Dict[str, int] = {}
        self._engine_counts: Dict[str, int] = {}

    def record_api_call(self, endpoint: str) -> None:
        self._api_counts[endpoint] = self._api_counts.get(endpoint, 0) + 1

    def record_engine_execution(self, engine_name: str) -> None:
        self._engine_counts[engine_name] = self._engine_counts.get(engine_name, 0) + 1

    def get_metrics_summary(self) -> Dict[str, Any]:
        return {
            "api_calls": self._api_counts,
            "engine_executions": self._engine_counts,
        }


metrics_collector = MetricsCollector()
