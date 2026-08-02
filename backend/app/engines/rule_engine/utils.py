def match_answer_pattern(given_answer: str, pattern: str) -> bool:
    return given_answer.strip().lower() == pattern.strip().lower()
