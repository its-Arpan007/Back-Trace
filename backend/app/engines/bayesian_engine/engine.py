from typing import Dict, Any, List, Tuple
from app.domain.interfaces.engine import IEngine
from app.engines.bayesian_engine.interfaces import IBayesianEngine


class BayesianEngine(IEngine, IBayesianEngine):
    """Production Bayesian Knowledge Tracing (BKT) Engine updating posterior knowledge probability P(L_t | Obs)."""

    def __init__(self):
        # Default BKT parameters
        self.p_init = 0.20
        self.p_transit = 0.15
        self.p_slip = 0.10
        self.p_guess = 0.20

    @property
    def name(self) -> str:
        return "Bayesian Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return []

    async def calculate_posterior(
        self,
        p_know: float,
        is_correct: bool,
        p_transit: float = 0.15,
        p_slip: float = 0.10,
        p_guess: float = 0.20,
    ) -> Tuple[float, float]:
        """Calculates P(L_t | Obs) and updates P(L_{t+1}) after transition step."""
        if is_correct:
            p_obs_given_know = 1.0 - p_slip
            p_obs_given_not_know = p_guess
        else:
            p_obs_given_know = p_slip
            p_obs_given_not_know = 1.0 - p_guess

        # Bayes rule
        numerator = p_know * p_obs_given_know
        denominator = numerator + ((1.0 - p_know) * p_obs_given_not_know)
        p_know_given_obs = numerator / max(denominator, 1e-9)

        # Transition step: P(L_{t+1}) = P(L_t | Obs) + (1 - P(L_t | Obs)) * P(T)
        p_next = p_know_given_obs + ((1.0 - p_know_given_obs) * p_transit)
        return round(p_know_given_obs, 4), round(p_next, 4)

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        p_know = input_data.get("p_know", self.p_init)
        is_correct = input_data.get("is_correct", True)
        post, p_next = await self.calculate_posterior(p_know, is_correct)
        return {
            "p_know_before": p_know,
            "is_correct": is_correct,
            "p_know_posterior": post,
            "p_know_next": p_next,
        }

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
