from dataclasses import dataclass


@dataclass(frozen=True)
class DifficultyValueObject:
    level: str

    VALID_LEVELS = {"easy", "medium", "hard", "advanced", "expert"}

    def __post_init__(self):
        norm_level = self.level.lower().strip()
        if norm_level not in self.VALID_LEVELS:
            raise ValueError(f"Invalid difficulty level: {self.level}. Must be one of {self.VALID_LEVELS}")
        object.__setattr__(self, 'level', norm_level)
