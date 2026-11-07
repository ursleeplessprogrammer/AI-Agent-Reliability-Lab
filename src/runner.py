import json
from pathlib import Path

from src.agent import MockAgent
from src.evaluator import evaluate_result
from src.metrics import calculate_metrics
from src.models import Scenario


def load_scenarios(path: Path) -> list[Scenario]:
    """Load test scenarios from a JSON file."""
    if not path.exists():
        raise FileNotFoundError(f"Scenario file not found: {path}")

    records = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(records, list):
        raise ValueError("Scenario JSON must contain a list.")

    return [Scenario(**record) for record in records]


def run_evaluation(
    scenarios: list[Scenario],
) -> tuple[list[dict], dict]:
    """Run the agent against all scenarios and evaluate the results."""
    agent = MockAgent()
    results = []

    for scenario in scenarios:
        agent_result = agent.run(scenario)
        results.append(evaluate_result(scenario, agent_result))

    metrics = calculate_metrics(results)
    return results, metrics
