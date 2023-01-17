from datetime import date
from subprocess import CalledProcessError, run

import sphinx_rtd_theme  # noqa: F401

project = "Nissan Leaf OBD-II manual"
author = "Seth Fischer"
project_copyright = f"{date.today().year}, {author}"

try:
    process = run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, encoding="ascii"
    )
    revision = process.stdout.strip()
except CalledProcessError:
    revision = None

version = date.today().strftime("%Y.%-m.%-d")

if revision is not None:
    release = "{}+{}".format(version, revision)
else:
    release = version


exclude_patterns = [
    "code/*",
    "includes/*",
]
extensions = [
    "sphinx_rtd_theme",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.spelling",
]
math_eqref_format = "Equation ({number})"
nitpicky = True
numfig = True
numfig_format = {"figure": "Figure %s"}
templates_path = ["_templates"]
trim_footnote_reference_space = True


html_show_copyright = False
html_show_sphinx = False
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_title = project
html_use_index = True


latex_appendices = [
    "related",
    "glossary",
    "disclaimer",
    "license",
    "z-bibliography",
]
latex_documents = [
    (
        "index.latex",
        "leaf-obd.tex",
        project,
        author,
        "manual",
        False,
    ),
]
latex_elements = {
    "papersize": "a4paper",
    "preamble": r"""
\usepackage{CJKutf8}
\newcommand*{\OBDtwo}{OBD-\uppercase\expandafter{\romannumeral 2}}
\setcounter{tocdepth}{1}
\DeclareUnicodeCharacter{022C5}{\ensuremath{\cdot}}
""",
}
latex_show_pagerefs = True
latex_show_urls = "footnote"


bibtex_bibfiles = ["bibliography.bib"]


linkcheck_ignore = [
    r"http://www.leafspypro.com/",  # persistent DNS time-outs
]


spelling_exclude_patterns = [
    "disclaimer.rst",  # contains Japanese characters
]
spelling_lang = "en_GB"
spelling_word_list_filename = "wordlist.txt"
tokenizer_lang = "en_GB"
