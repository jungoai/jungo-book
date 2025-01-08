import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'My Docs Project'
author = 'Your Name'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Specify file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Optional: Add Markdown-specific configurations
myst_enable_extensions = [
    "deflist",  # Enable definition lists
    "linkify",  # Automatically turn URLs into links
    "colon_fence",  # Enable ::: for block elements
]

templates_path = ['_templates']

html_theme = 'alabaster'  # Or 'sphinx_rtd_theme' for the RTD theme
html_static_path = ['_static']
