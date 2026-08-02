from dataclasses import dataclass


@dataclass(frozen=True)
class ScoreValueObject:
    value: float

    def __post_init__(self):
        if not (0.0 <= self.value <= 1.0):
            raise ValueError("Score must be between 0.0 and 1.0")

    @property
    def percentage(self) -> float:
        return round(self.value * 100, 2)
