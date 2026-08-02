from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class BacktraceException(Exception):
    """Base exception class for BACKTRACE platform."""

    def __init__(self, message: str, code: str = "INTERNAL_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)


class NotFoundException(BacktraceException):
    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            message=f"{resource} with id '{identifier}' not found.",
            code="NOT_FOUND",
        )


class UnauthorizedException(BacktraceException):
    def __init__(self, message: str = "Authentication credentials were not provided or are invalid."):
        super().__init__(message=message, code="UNAUTHORIZED")


class ForbiddenException(BacktraceException):
    def __init__(self, message: str = "You do not have permission to perform this operation."):
        super().__init__(message=message, code="FORBIDDEN")


class ValidationException(BacktraceException):
    def __init__(self, message: str, errors: Optional[Dict[str, Any]] = None):
        self.errors = errors
        super().__init__(message=message, code="VALIDATION_ERROR")
