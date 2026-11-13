import unittest

from scripts.check_catalog import broken_anchors, heading_slug, split_table_row


class MarkdownParsingTests(unittest.TestCase):
    def test_table_row_respects_inline_code_pipe(self):
        self.assertEqual(
            split_table_row("| [Tool](https://example.com) | Uses `a|b` internally |"),
            ["[Tool](https://example.com)", "Uses `a|b` internally"],
        )

    def test_table_row_respects_escaped_pipe(self):
        self.assertEqual(
            split_table_row(r"| Tool | left \| right |"),
            ["Tool", r"left \| right"],
        )

    def test_heading_slug_handles_emoji_and_words(self):
        self.assertEqual(heading_slug("🌐 Browser and Desktop Agents"), "-browser-and-desktop-agents")

    def test_heading_slug_matches_github_for_slash(self):
        # GitHub does not collapse whitespace: "/" is stripped, leaving two
        # spaces that each become a hyphen.
        self.assertEqual(heading_slug("Lightweight / Minimalist"), "lightweight--minimalist")

    def test_anchor_checker_accepts_current_heading_and_reports_missing_one(self):
        text = "## 🌐 Browser and Desktop Agents\n\n[Good](#-browser-and-desktop-agents) [Bad](#missing)\n"
        self.assertEqual(
            broken_anchors(text),
            ["Line 3: unresolved in-file anchor '#missing'."],
        )


if __name__ == "__main__":
    unittest.main()
