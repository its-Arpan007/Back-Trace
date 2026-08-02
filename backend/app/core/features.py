from typing import Dict
from pydantic import BaseModel


class FeatureFlags(BaseModel):
    ENABLE_KNOWLEDGE_GRAPH: bool = True
    ENABLE_AI_EXPLANATION: bool = True
    ENABLE_RECOMMENDATION_ENGINE: bool = True
    ENABLE_ANALYTICS: bool = True
    ENABLE_REDIS_CACHE: bool = True
    ENABLE_EXPERIMENTAL_FEATURES: bool = False


class FeatureManager:
    def __init__(self, flags: FeatureFlags = FeatureFlags()):
        self._flags = flags

    def is_enabled(self, feature_name: str) -> bool:
        attr_name = f"ENABLE_{feature_name.upper()}"
        return getattr(self._flags, attr_name, False)

    def set_feature(self, feature_name: str, enabled: bool) -> None:
        attr_name = f"ENABLE_{feature_name.upper()}"
        if hasattr(self._flags, attr_name):
            setattr(self._flags, attr_name, enabled)

    def all_flags(self) -> Dict[str, bool]:
        return self._flags.model_dump()


feature_manager = FeatureManager()
