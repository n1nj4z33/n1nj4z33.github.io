# -*- coding: utf-8 -*-
"""
App settings
"""
import os

# REPO_NAME = ""
DEBUG = True
SECRET_KEY = "n1nj4z33"

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    """Return the parent of a directory."""
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)

FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, "build")
FREEZER_REMOVE_EXTRA_FILES = False

FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite"]
FLATPAGES_ROOT = os.path.join(PROJECT_ROOT, "n1nj4z33-pages")
FLATPAGES_EXTENSION = ".md"
