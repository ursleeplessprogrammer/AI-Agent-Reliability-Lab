from statistics import mean


def calculate_metrics(results: list[dict]) -> dict:
    """Calculate aggregate and category-level evaluation metrics."""
    if not results:
        return {
            "scenario_count": 0,
            "pass_count": 0,
            "pass_rate": 0.0,
            "average_latency_ms": 0.0,
            "by_category": {},
        }

    pass_count = sum(bool(result["passed"]) for result in results)
    latencies = [result["latency_ms"] for result in results]

    category_metrics = {}

    categories = sorted({result["category"] for result in results})
    for category in categories:
        group = [
            result for result in results
            if result["category"] == category
        ]
        group_passes = sum(bool(result["passed"]) for result in group)

        category_metrics[category] = {
            "scenario_count": len(group),
            "pass_count": group_passes,
            "pass_rate": round(group_passes / len(group), 3),
        }

    return {
        "scenario_count": len(results),
        "pass_count": pass_count,
        "pass_rate": round(pass_count / len(results), 3),
        "average_latency_ms": round(mean(latencies), 2),
        "by_category": category_metrics,
    }
