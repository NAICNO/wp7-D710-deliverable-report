"""
Markdown quality checks for D7.10-report.md.

Validates structural properties of the report markdown.
"""

import re

import pytest

from conftest import REPORT_PATH


def _load_report() -> str:
    with open(REPORT_PATH, encoding="utf-8") as fh:
        return fh.read()


def _load_lines() -> list[str]:
    with open(REPORT_PATH, encoding="utf-8") as fh:
        return fh.readlines()


class TestMarkdownStructure:
    def test_starts_with_heading(self):
        lines = _load_lines()
        assert lines[0].startswith("# "), "Report must start with a level-1 heading"

    def test_has_level_2_headings(self):
        text = _load_report()
        h2_matches = re.findall(r"^## .+", text, re.MULTILINE)
        assert len(h2_matches) >= 4, "Report must have at least 4 level-2 headings"

    def test_has_tables(self):
        text = _load_report()
        table_rows = re.findall(r"^\|.+\|$", text, re.MULTILINE)
        assert len(table_rows) >= 10, "Report must contain tables"

    def test_no_broken_links(self):
        text = _load_report()
        links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", text)
        for link_text, link_url in links:
            assert len(link_text.strip()) > 0, f"Link with URL '{link_url}' has empty text"
            assert len(link_url.strip()) > 0, f"Link '{link_text}' has empty URL"

    def test_report_length_reasonable(self):
        lines = _load_lines()
        assert len(lines) >= 200, "Report must be at least 200 lines"

    def test_no_todo_markers(self):
        text = _load_report()
        assert "TODO" not in text, "Report must not contain TODO markers"

    def test_no_placeholder_text(self):
        text = _load_report()
        assert "Lorem ipsum" not in text
