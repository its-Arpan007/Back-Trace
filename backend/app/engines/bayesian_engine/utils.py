def compute_bkt_posterior(p_know: float, p_slip: float, p_guess: float, is_correct: bool) -> float:
    if is_correct:
        numerator = p_know * (1 - p_slip)
        denominator = (p_know * (1 - p_slip)) + ((1 - p_know) * p_guess)
    else:
        numerator = p_know * p_slip
        denominator = (p_know * p_slip) + ((1 - p_know) * (1 - p_guess))
    return numerator / denominator if denominator > 0 else p_know
