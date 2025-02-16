# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os, sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

def setup(app):
    app.add_config_value('releaselevel', '', 'env')
    
DATA = None
PYPROJECT = os.path.join("..", "..", "Cargo.toml")
with open(PYPROJECT, "r", encoding="utf8") as f:
    pyproject = f.read()
    DATA = tomllib.loads(pyproject)
PROJECT_VERSION = DATA["package"]["version"]
PROJECT_NAME = DATA["package"]["name"]
AUTHOR_TABLE = DATA["package"]["authors"]
AUTHORS = ",".join([f"{aut}" for aut in AUTHOR_TABLE])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "HydroRoll"  # PROJECT_NAME
release = PROJECT_VERSION  # "latest"
copyright = "2023-PRESENT, HydroRoll-Team."
author = AUTHORS  # "Hsiang Nianian"

# html_title = "HydroRoll Docs"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.imgmath",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.httpdomain",
    "sphinx.ext.ifconfig",
    "myst_parser",
]

doctest_global_setup = '''
try:
    import hydro_roll as hr
    import hydro_roll_core as hrc
except ImportError:
    hr = None
    hrc = None
'''
todo_include_todos = True
todo_emit_warnings = True
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extlinks = {
    "issue": ("https://github.com/HydroRoll-Team/HydroRoll/issues/%s", "[issue %s]"),
}
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
rst_prolog = """
.. ifconfig:: releaselevel in ('alpha', 'beta', 'rc')

   .. warning::
   
        This stuff is only included in the built docs for unstable versions.

"""
rst_epilog = """
.. |psf| replace:: Python Software Foundation
"""
locale_dirs = ["../locales/"]  # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.
numfig = True # Figures, tables and code blocks are automatically numbered if they have a title
pygments_style = "rrt" # default sphinx, change the style of code block
math_number_all = True # Number all equations, figures, tables and code blocks
html_additional_pages = {
    'copy': 'copying.html',
}
html_split_index = True # Split the index page by each alphabet
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["../_static"]
_html_logo = (
    "https://cdn.jsdelivr.net/gh/HydroRoll-Team/HydroRoll@main/docs/_static/logo.png"
)
# html_logo = _html_logo
html_favicon = _html_logo

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_copy_source = True
html_show_sourcelink = True

html_theme_options = {
    "announcement": "<em><a href='#'>documentation</a> is still under construction now, welcome any <a href='contributing.html'>contribution</a>!</em>",
    "source_repository": "https://github.com/HydroRoll-Team/HydroRoll/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    # Toc options
    # "collapse_navigation": True,
    # "sticky_navigation": False,
    # "navigation_depth": 1,
    # "includehidden": False,
    # "titles_only": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/HydroRoll-Team/HydroRoll/",
            "html": "",
            "class": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/hydro_roll/",
            "html": "",
            "class": "fa-brands fa-python",
        },
    ],
}

# html_sidebars = {
#    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html', 'relations.html'],
#    'using/windows': ['windowssidebar.html', 'searchbox.html'],
# }