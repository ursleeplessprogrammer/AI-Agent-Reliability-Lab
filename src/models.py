from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Scenario:
    id: str
    category: str
    prompt: str
    expected_tool: str | None = None
    expected_answer_contains: str | None = None
    must_not_call: list[str] = field(default_factory=list)
    require_human_approval: bool = False


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]


@dataclass
class AgentResult:
    scenario_id: str
    answer: str
    tool_calls: list[ToolCall] = field(default_factory=list)
    requires_human_approval: bool = False
    latency_ms: float = 0.0
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
