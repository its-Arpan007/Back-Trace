def score_to_mastery_level(score: float) -> str:
    if score >= 0.9:
        return "master"
    elif score >= 0.75:
        return "proficient"
    elif score >= 0.5:
        return "developing"
    return "novice"
