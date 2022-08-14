# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime
# Import proj's meta info
sys.path.insert(0, os.path.abspath('../sphinxnotes'))
import mock as proj

# -- Project information -----------------------------------------------------

project = proj.__title__
copyright = '%s, %s' % (datetime.now().year, proj.__author__)
author = proj.__author__

# The full version, including alpha/beta/rc tags
version = release = proj.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'mock',
    'sphinx.ext.githubpages',
]

mock_directives = [
    'contents',
    'foo',
    ('bar', 'literal'),
]

# If true, keep warnings as “system message” paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
keep_warnings = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

html_theme_options = {
    'repository_url': 'https://github.com/sphinx-notes/mock',
    "use_repository_button": True,
    "use_download_button": False,
    "single_page": True
}

# The URL which points to the root of the HTML documentation.
# It is used to indicate the location of document like canonical_url
html_baseurl = proj.__url__

html_logo = html_favicon = '_images/sphinx-notes.png'
