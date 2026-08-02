import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("backtrace.http")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()
        request_id = getattr(request.state, "request_id", "N/A")

        logger.info(
            f"[{request_id}] Incoming request {request.method} {request.url.path}"
        )

        try:
            response = await call_next(request)
            process_time = (time.time() - start_time) * 1000
            logger.info(
                f"[{request_id}] Completed {request.method} {request.url.path} "
                f"Status: {response.status_code} in {process_time:.2f}ms"
            )
            return response
        except Exception as exc:
            process_time = (time.time() - start_time) * 1000
            logger.error(
                f"[{request_id}] Failed {request.method} {request.url.path} "
                f"in {process_time:.2f}ms - Exception: {exc}"
            )
            raise
