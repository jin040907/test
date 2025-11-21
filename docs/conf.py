# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Conf Parser Workspace'
copyright = '2024, Open Source Software Introduction'
author = 'Conf Parser Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['../_static', '../assets']
html_css_files = ['css/style.css']

# Use the existing custom styling
html_style = None

# HTML options
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../scripts'))

# -- Options for autodoc -----------------------------------------------------

autodoc_mock_imports = ['js-yaml']

# -- Intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Custom configuration ----------------------------------------------------

# Master document
master_doc = 'index'

# HTML title
html_title = 'Conf Parser Workspace Documentation'

# HTML logo (optional)
# html_logo = '../_static/sample-image.svg'

# Favicon (optional)
# html_favicon = '../_static/favicon.ico'

