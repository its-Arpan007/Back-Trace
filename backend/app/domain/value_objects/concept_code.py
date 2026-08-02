from dataclasses import dataclass


@dataclass(frozen=True)
class ConceptCodeValueObject:
    code: str

    def __post_init__(self):
        if not self.code or len(self.code.strip()) == 0:
            raise ValueError("Concept code cannot be empty")
        object.__setattr__(self, 'code', self.code.upper().strip())
