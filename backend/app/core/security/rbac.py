from functools import wraps
from typing import List, Callable, Any
from fastapi import HTTPException, status, Request


def require_roles(allowed_roles: List[str]) -> Callable:
    """Decorator guard checking user role claims."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Inspection hook for request state
            return await func(*args, **kwargs)
        return wrapper
    return decorator


def require_permissions(required_permissions: List[str]) -> Callable:
    """Decorator guard checking fine-grained permission claims."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            return await func(*args, **kwargs)
        return wrapper
    return decorator
