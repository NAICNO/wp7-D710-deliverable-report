"""
Episode content validation tests.

Verifies that each episode follows the sphinx-lesson format with
objectives, keypoints, and expected content.
"""

import os
import re

import pytest

from conftest import EPISODES_DIR, EPISODE_FILES, USE_CASES, UC_IDS


def _load_episode(filename: str) -> str:
    path = os.path.join(EPISODES_DIR, filename)
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# All episodes: structural checks
# ---------------------------------------------------------------------------


class TestEpisodeStructure:
    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_starts_with_heading(self, filename):
        text = _load_episode(filename)
        assert text.startswith("# "), f"{filename} must start with a level-1 heading"

    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_has_objectives(self, filename):
        text = _load_episode(filename)
        assert "```{objectives}" in text, f"{filename} must have objectives block"

    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_has_keypoints(self, filename):
        text = _load_episode(filename)
        assert "```{keypoints}" in text, f"{filename} must have keypoints block"

    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_minimum_length(self, filename):
        text = _load_episode(filename)
        lines = text.strip().split("\n")
        assert len(lines) >= 20, f"{filename} must have at least 20 lines"


# ---------------------------------------------------------------------------
# Use case episodes: each must reference the correct repository
# ---------------------------------------------------------------------------

UC_EPISODE_MAP = [
    ("04-uc1-climate-teleconnection.md", "UC1", "wp7-UC1-climate-indices-teleconnection"),
    ("05-uc2-pem-electrolyzer.md", "UC2", "wp7-UC2-pem-electrolyzer-digital-twin"),
    ("06-uc3-pseudo-hamiltonian.md", "UC3", "wp7-UC3-pseudo-hamiltonian-neural-networks"),
    ("07-uc4-medical-imaging.md", "UC4", "wp7-UC4-medical-image-registration"),
    ("08-uc5-ais-classification.md", "UC5", "wp7-UC5-ais-classification-gnn"),
    ("09-uc6-multimodal-optimization.md", "UC6", "wp7-UC6-multimodal-optimization"),
    ("10-uc7-latent-pde.md", "UC7", "wp7-UC7-latent-pde-representation"),
]


class TestUseCaseEpisodes:
    @pytest.mark.parametrize(
        "filename,uc_id,repo",
        UC_EPISODE_MAP,
        ids=[x[1] for x in UC_EPISODE_MAP],
    )
    def test_references_repository(self, filename, uc_id, repo):
        text = _load_episode(filename)
        assert repo in text, f"{filename} must reference repository '{repo}'"

    @pytest.mark.parametrize(
        "filename,uc_id,repo",
        UC_EPISODE_MAP,
        ids=[x[1] for x in UC_EPISODE_MAP],
    )
    def test_has_problem_section(self, filename, uc_id, repo):
        text = _load_episode(filename)
        assert "## The Problem" in text or "## Approach" in text, (
            f"{filename} must have a Problem or Approach section"
        )

    @pytest.mark.parametrize(
        "filename,uc_id,repo",
        UC_EPISODE_MAP,
        ids=[x[1] for x in UC_EPISODE_MAP],
    )
    def test_has_quick_start(self, filename, uc_id, repo):
        text = _load_episode(filename)
        assert "Quick Start" in text or "git clone" in text, (
            f"{filename} must have a Quick Start section or clone command"
        )


# ---------------------------------------------------------------------------
# Introduction episode
# ---------------------------------------------------------------------------


class TestIntroductionEpisode:
    def test_mentions_all_use_cases(self):
        text = _load_episode("01-introduction.md")
        for uc_id in UC_IDS:
            assert uc_id in text, f"Introduction must mention {uc_id}"

    def test_has_technology_table(self):
        text = _load_episode("01-introduction.md")
        assert "PyTorch" in text
        assert "TensorFlow" in text

    def test_has_contributor_info(self):
        text = _load_episode("01-introduction.md")
        assert "NORCE" in text
        assert "SINTEF" in text
        assert "UiB" in text


# ---------------------------------------------------------------------------
# VM provisioning episode
# ---------------------------------------------------------------------------


class TestVMProvisioningEpisode:
    def test_mentions_orchestrator(self):
        text = _load_episode("02-provision-vm.md")
        assert "orchestrator.naic.no" in text

    def test_mentions_myaccessid(self):
        text = _load_episode("02-provision-vm.md")
        assert "MyAccessID" in text

    def test_has_ssh_instructions(self):
        text = _load_episode("02-provision-vm.md")
        assert "ssh -i" in text

    def test_has_windows_instructions(self):
        text = _load_episode("02-provision-vm.md")
        assert "Windows" in text


# ---------------------------------------------------------------------------
# Getting started episode
# ---------------------------------------------------------------------------


class TestGettingStartedEpisode:
    def test_has_clone_commands(self):
        text = _load_episode("03-getting-started.md")
        assert "git clone" in text

    def test_has_jupyter_instructions(self):
        text = _load_episode("03-getting-started.md")
        assert "jupyter" in text.lower()

    def test_mentions_agent_md(self):
        text = _load_episode("03-getting-started.md")
        assert "AGENT.md" in text


# ---------------------------------------------------------------------------
# Common patterns episode
# ---------------------------------------------------------------------------


class TestCommonPatternsEpisode:
    def test_physics_informed_pattern(self):
        text = _load_episode("11-common-patterns.md")
        assert "physics-informed" in text.lower()

    def test_data_representation_pattern(self):
        text = _load_episode("11-common-patterns.md")
        assert "data representation" in text.lower()

    def test_reproducibility_pattern(self):
        text = _load_episode("11-common-patterns.md")
        assert "reproducibility" in text.lower()

    def test_infrastructure_pattern(self):
        text = _load_episode("11-common-patterns.md")
        assert "NAIC infrastructure" in text


# ---------------------------------------------------------------------------
# FAQ episode
# ---------------------------------------------------------------------------


class TestFAQEpisode:
    def test_has_gpu_requirements(self):
        text = _load_episode("12-faq.md")
        assert "GPU" in text

    def test_has_python_version(self):
        text = _load_episode("12-faq.md")
        assert "Python 3.11" in text

    def test_has_contact_info(self):
        text = _load_episode("12-faq.md")
        assert "support@naic.no" in text


# ---------------------------------------------------------------------------
# Sphinx config and index
# ---------------------------------------------------------------------------


class TestSphinxConfig:
    def test_conf_py_has_sphinx_lesson(self):
        path = os.path.join(EPISODES_DIR, "..", "conf.py")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        assert "sphinx_lesson" in text

    def test_conf_py_has_mermaid(self):
        path = os.path.join(EPISODES_DIR, "..", "conf.py")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        assert "sphinxcontrib.mermaid" in text

    def test_index_rst_references_all_episodes(self):
        path = os.path.join(EPISODES_DIR, "..", "index.rst")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for ep in EPISODE_FILES:
            assert ep in text, f"index.rst must reference {ep}"
