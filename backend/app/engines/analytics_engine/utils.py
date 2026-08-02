def compute_accuracy(correct: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round((correct / total), 4)
