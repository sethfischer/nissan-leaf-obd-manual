import sphinx_rtd_theme

project = "Nissan Leaf OBD-II guide"
author = "Seth Fischer"
copyright = "2020, Seth Fischer"

release = "0.1.0"

extensions = [
    "sphinx_rtd_theme",
    "sphinxcontrib.bibtex",
]
nitpicky = True
numfig = True
templates_path = ["_templates"]


html_show_copyright = False
html_show_sphinx = False
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"


latex_elements = {
    "papersize": "a4paper",
    "preamble": r"""
\usepackage{CJKutf8}
\newcommand*{\OBDtwo}{OBD-\uppercase\expandafter{\romannumeral 2}}
""",
}
latex_engine = "platex"
latex_use_xindy = False
