from typing import Dict, Any
from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    status: str = Field(..., example="healthy")
    environment: str = Field(..., example="development")
    version: str = Field(..., example="0.1.0")
    database_connected: bool = Field(..., example=True)
    redis_connected: bool = Field(..., example=True)
    details: Dict[str, Any] = Field(default_factory=dict)
