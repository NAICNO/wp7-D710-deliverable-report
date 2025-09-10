"""
Project structure validation tests.

Verifies that all expected files and directories exist.
"""

import os

import pytest

from conftest import (
    CONTENT_DIR,
    EPISODES_DIR,
    EPISODE_FILES,
    PROJECT_ROOT,
    README_PATH,
    REPORT_PATH,
)


class TestRootLevelFiles:
    def test_readme_exists(self):
        assert os.path.isfile(README_PATH), "README.md must exist"

    def test_readme_is_not_empty(self):
        assert os.path.getsize(README_PATH) > 0, "README.md must not be empty"

    def test_report_exists(self):
        assert os.path.isfile(REPORT_PATH), "D7.10-report.md must exist"

    def test_report_is_not_empty(self):
        assert os.path.getsize(REPORT_PATH) > 0, "D7.10-report.md must not be empty"

    def test_tests_dir_exists(self):
        assert os.path.isdir(os.path.join(PROJECT_ROOT, "tests"))


class TestContentDirectory:
    def test_content_dir_exists(self):
        assert os.path.isdir(CONTENT_DIR), "content/ directory must exist"

    def test_conf_py_exists(self):
        assert os.path.isfile(os.path.join(CONTENT_DIR, "conf.py"))

    def test_index_rst_exists(self):
        assert os.path.isfile(os.path.join(CONTENT_DIR, "index.rst"))

    def test_episodes_dir_exists(self):
        assert os.path.isdir(EPISODES_DIR), "content/episodes/ must exist"

    def test_static_dir_exists(self):
        assert os.path.isdir(os.path.join(CONTENT_DIR, "_static"))

    def test_images_dir_exists(self):
        assert os.path.isdir(os.path.join(CONTENT_DIR, "images"))

    def test_downloads_dir_exists(self):
        assert os.path.isdir(os.path.join(CONTENT_DIR, "downloads"))

    def test_downloads_index_exists(self):
        assert os.path.isfile(
            os.path.join(CONTENT_DIR, "downloads", "index.rst")
        )


class TestEpisodeFiles:
    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_episode_exists(self, filename):
        path = os.path.join(EPISODES_DIR, filename)
        assert os.path.isfile(path), f"Episode {filename} must exist"

    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_episode_is_not_empty(self, filename):
        path = os.path.join(EPISODES_DIR, filename)
        assert os.path.getsize(path) > 0, f"Episode {filename} must not be empty"

    @pytest.mark.parametrize("filename", EPISODE_FILES)
    def test_episode_has_md_extension(self, filename):
        assert filename.endswith(".md"), f"{filename} must have .md extension"

    def test_twelve_episodes_present(self):
        md_files = [
            f for f in os.listdir(EPISODES_DIR) if f.endswith(".md")
        ]
        assert len(md_files) == 12, f"Expected 12 episodes, found {len(md_files)}"
