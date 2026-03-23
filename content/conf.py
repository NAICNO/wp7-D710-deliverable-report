# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'D7.10 — Summary of Completed Demonstrators'
copyright = '2026, NAIC / NORCE / Sigma2'
author = 'NAIC WP7 Team'
release = '1.0'

# Logo setup
html_logo = 'images/NRIS-Logo.png'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.mermaid',
    'sphinx_lesson',
    'sphinx.ext.githubpages',
    'sphinx_tabs.tabs',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
sphinx_tabs_disable_css_loading = True

html_static_path = ['_static']
html_css_files = [
    'tabs.css',
]
