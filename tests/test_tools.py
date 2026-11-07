import unittest

from src.tools import run_tool


class ToolTests(unittest.TestCase):
    def test_search_finds_release_date(self):
        result = run_tool(
            "search_knowledge_base",
            {"query": "Find the project release date."},
        )
        self.assertIn("April 15, 2026", result)

    def test_unknown_tool_is_rejected(self):
        with self.assertRaises(ValueError):
            run_tool("send_email", {})


if __name__ == "__main__":
    unittest.main()
