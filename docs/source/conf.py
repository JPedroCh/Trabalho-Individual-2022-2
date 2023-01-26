# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# sys.path.append("/Users/jpedroch/Documents/GCES/MEU/Trabalho-Individual-2022-2/ext/breathe")

project = 'Pynalytics'
copyright = '2023, João Pedro Chaves'
author = 'João Pedro Chaves'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.viewcode','breathe']


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = 'alabaster'
html_static_path = ['../_static']

breathe_projects = { "pynalytics" : "../../docs_xml/xml", }
