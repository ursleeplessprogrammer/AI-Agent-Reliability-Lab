import argparse
import json
from pathlib import Path

from src.runner import load_scenarios, run_evaluation


ROOT_DIR = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(
        description="Run the AI Agent Reliability Lab evaluation."
    )
    parser.add_argument(
        "--scenarios",
        type=Path,
        default=ROOT_DIR / "data" / "scenarios.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT_DIR / "output",
    )
    args = parser.parse_args()

    scenarios = load_scenarios(args.scenarios)
    results, metrics = run_evaluation(scenarios)

    args.output.mkdir(parents=True, exist_ok=True)

    results_path = args.output / "scenario_results.json"
    metrics_path = args.output / "metrics.json"

    results_path.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )
    metrics_path.write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8",
    )

    print("AI Agent Reliability Lab")
    print("------------------------")
    print(f"Scenarios:          {metrics['scenario_count']}")
    print(f"Passed:             {metrics['pass_count']}")
    print(f"Pass rate:          {metrics['pass_rate']:.1%}")
    print(f"Average latency:    {metrics['average_latency_ms']:.2f} ms")
    print(f"Results:            {results_path}")
    print(f"Metrics:            {metrics_path}")

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"{status:4} {result['scenario_id']} ({result['category']})")


if __name__ == "__main__":
    main()
