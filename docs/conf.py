"""Sphinx configuration."""
project = "slack_status_updater"
author = "Michal Halenka"
copyright = "2022, Michal Halenka"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
