from datetime import date
from subprocess import CalledProcessError, run

import sphinx_rtd_theme

project = "Nissan Leaf OBD-II guide"
author = "Seth Fischer"
copyright = "2020, Seth Fischer"

try:
    process = run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, encoding="ascii"
    )
    revision = process.stdout.strip()
except CalledProcessError as error:
    revision = None

version = date.today().strftime("%Y.%-m.%-d")

if revision is not None:
    release = "{}+{}".format(version, revision)
else:
    release = version


extensions = [
    "sphinx_rtd_theme",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.spelling",
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


spelling_exclude_patterns = [
    "disclaimer.rst",  # contains Japanese characters
]
spelling_lang = "en_GB"
spelling_word_list_filename = "wordlist.txt"
tokenizer_lang = "en_GB"
