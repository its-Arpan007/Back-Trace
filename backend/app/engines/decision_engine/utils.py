def determine_difficulty_adjustment(current: str, is_correct: bool) -> str:
    levels = ["easy", "medium", "hard", "advanced", "expert"]
    try:
        idx = levels.index(current.lower())
    except ValueError:
        idx = 1

    if is_correct and idx < len(levels) - 1:
        return levels[idx + 1]
    elif not is_correct and idx > 0:
        return levels[idx - 1]
    return levels[idx]
