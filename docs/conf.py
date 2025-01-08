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

templates_path = ['_templates']

html_theme = 'alabaster'  # Or 'sphinx_rtd_theme' for the RTD theme
html_static_path = ['_static']
