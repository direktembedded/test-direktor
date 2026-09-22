# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test Direktor ™ Application'
copyright = 'Copyright © 2025 Direkt Embedded Pty Ltd'
author = 'Direkt Embedded Pty Ltd'

# We use this release as the documentation release
release = version = '0.4.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['../_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['../_static']

#latex_toplevel_sectioning = 'section'

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}
