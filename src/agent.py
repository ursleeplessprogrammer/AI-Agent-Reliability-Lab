from time import perf_counter

from src.models import AgentResult, Scenario, ToolCall
from src.tools import run_tool


UNSAFE_TERMS = [
    "email all customer records",
    "send all customer records",
    "export customer records",
]


class MockAgent:
    """
    Deterministic agent used to test the evaluation pipeline.

    This is not a language model. Replace it with a real model adapter
    only after the evaluation and safety harness is working.
    """

    def run(self, scenario: Scenario) -> AgentResult:
        start = perf_counter()
        prompt = scenario.prompt.lower()

        if any(term in prompt for term in UNSAFE_TERMS):
            return AgentResult(
                scenario_id=scenario.id,
                answer="I cannot send or disclose customer records.",
                requires_human_approval=True,
                latency_ms=(perf_counter() - start) * 1000,
            )

        call = ToolCall(
            name="search_knowledge_base",
            arguments={"query": scenario.prompt},
        )

        try:
            answer = run_tool(call.name, call.arguments)
            tool_calls = [call]
            error = None
        except Exception as exc:
            answer = "I could not complete the request."
            tool_calls = [call]
            error = str(exc)

        return AgentResult(
            scenario_id=scenario.id,
            answer=answer,
            tool_calls=tool_calls,
            requires_human_approval=False,
            latency_ms=(perf_counter() - start) * 1000,
            error=error,
        )
