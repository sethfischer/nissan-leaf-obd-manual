import sphinx_rtd_theme

project = "Nissan Leaf OBD-II guide"
copyright = "2020, Seth Fischer"
author = "Seth Fischer"

release = "0.1.0"

extensions = [
    "sphinx_rtd_theme",
    "sphinxcontrib.bibtex",
]

templates_path = ["_templates"]

exclude_patterns = []

numfig = True

html_show_copyright = False
html_show_sphinx = False
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"

latex_engine = 'platex'
latex_use_xindy = False

latex_elements = {
    "papersize": "a4paper",
    'preamble': r'''
\usepackage{CJKutf8}
\newcommand*{\OBDtwo}{OBD-\uppercase\expandafter{\romannumeral 2}}
''',
}
