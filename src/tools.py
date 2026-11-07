from typing import Any


KNOWLEDGE_BASE = {
    "project release date": "The project release date is April 15, 2026.",
    "support hours": "Support hours are Monday through Friday, 9 AM to 5 PM.",
}


def search_knowledge_base(query: str) -> str:
    """Search a small, read-only example knowledge base."""
    normalized_query = query.lower()

    for key, value in KNOWLEDGE_BASE.items():
        if key in normalized_query or normalized_query in key:
            return value

    for key, value in KNOWLEDGE_BASE.items():
        if any(word in normalized_query for word in key.split()):
            return value

    return "No matching information was found in the knowledge base."


def run_tool(name: str, arguments: dict[str, Any]) -> str:
    """Execute an explicitly allowed tool."""
    if name == "search_knowledge_base":
        query = arguments.get("query", "")
        if not isinstance(query, str):
            raise ValueError("The search query must be text.")
        return search_knowledge_base(query)

    raise ValueError(f"Tool is not available: {name}")
