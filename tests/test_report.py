"""
D7.10 report content validation tests.

Verifies the report markdown has correct structure, covers all seven
use cases, contains required sections, and includes expected metadata.
"""

import re

import pytest

from conftest import REPORT_PATH, USE_CASES, UC_IDS


def _load_report() -> str:
    with open(REPORT_PATH, encoding="utf-8") as fh:
        return fh.read()


class TestReportMetadata:
    def test_has_title(self):
        text = _load_report()
        assert "# NAIC-deliverable-report-D7.10" in text

    def test_has_deliverable_id(self):
        text = _load_report()
        assert "Deliverable ID: D7.10" in text

    def test_has_document_owner(self):
        text = _load_report()
        assert "Document owner:" in text

    def test_has_work_package_wp7(self):
        text = _load_report()
        assert "Work-package(s): WP7" in text


REQUIRED_SECTIONS = [
    "Executive Summary",
    "Detailed Progress by Activity",
    "Common Patterns",
    "Deviations",
]


class TestReportSections:
    @pytest.mark.parametrize("section", REQUIRED_SECTIONS)
    def test_section_exists(self, section):
        text = _load_report()
        assert section in text, f"Report must contain section: {section}"


class TestUseCaseCoverage:
    @pytest.mark.parametrize("uc_id", UC_IDS)
    def test_use_case_mentioned(self, uc_id):
        text = _load_report()
        assert uc_id in text, f"Report must mention {uc_id}"

    @pytest.mark.parametrize(
        "uc",
        USE_CASES,
        ids=[uc["id"] for uc in USE_CASES],
    )
    def test_use_case_repo_linked(self, uc):
        text = _load_report()
        assert uc["repo"] in text, (
            f"Report must link to repo '{uc['repo']}' for {uc['id']}"
        )

    def test_all_seven_use_cases_in_table(self):
        text = _load_report()
        for i in range(1, 8):
            assert f"| **UC{i}**" in text, f"Status table must include UC{i}"


EXPECTED_GLOSSARY_TERMS = [
    "PINN", "PHNN", "GNN", "CEC2013", "PEM", "NAIC", "HPC", "SHGA",
]


class TestGlossary:
    def test_glossary_section_exists(self):
        text = _load_report()
        assert "Glossary" in text

    @pytest.mark.parametrize("term", EXPECTED_GLOSSARY_TERMS)
    def test_glossary_term_present(self, term):
        text = _load_report()
        assert f"**{term}**" in text, f"Glossary must define '{term}'"
