def sort_recommendations_by_priority(items: list) -> list:
    return sorted(items, key=lambda x: x.get("priority", 1), reverse=True)
