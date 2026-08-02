from dataclasses import dataclass


@dataclass
class BKTState:
    p_know: float = 0.5   # Prior probability of knowing concept
    p_transit: float = 0.1 # Probability of learning concept
    p_slip: float = 0.1    # Probability of slip given known
    p_guess: float = 0.2   # Probability of guess given unknown
