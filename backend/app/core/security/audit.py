import logging
from datetime import datetime, timezone
from typing import Dict, Any

audit_logger = logging.getLogger("backtrace.audit")


def log_security_event(event_type: str, actor_id: str, details: Dict[str, Any]) -> None:
    timestamp = datetime.now(timezone.utc).isoformat()
    audit_logger.info(
        f"[AUDIT] [{timestamp}] Event: {event_type} | Actor: {actor_id} | Details: {details}"
    )
