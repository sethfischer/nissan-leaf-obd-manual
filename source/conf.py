from datetime import date
from subprocess import CalledProcessError, run

import os
import sphinx_rtd_theme


DOC_SOURCES_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(DOC_SOURCES_DIR))


on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if on_rtd:
    RTD_SLUG = "leaf-obd"
    RTD_BIN_DIRECTORY = (
        "/home/docs/checkouts/readthedocs.org/user_builds/{}/envs/latest/bin".format(
            RTD_SLUG
        )
    )

    GIT_LFS_VERSION = "2.12.0"
    GIT_LFS_TAR_BALL = "git-lfs-linux-amd64-v{}.tar.gz".format(GIT_LFS_VERSION)
    GIT_LFS_TAR_BALL_URL = (
        "https://github.com/git-lfs/git-lfs/releases/download/v{}/{}".format(
            GIT_LFS_VERSION, GIT_LFS_TAR_BALL
        )
    )

    if not os.path.isfile(GIT_LFS_TAR_BALL):
        run(
            [
                "curl",
                "--location",
                "--silent",
                GIT_LFS_TAR_BALL_URL,
                "--output",
                GIT_LFS_TAR_BALL,
            ]
        )

    if not os.path.isfile("git-lfs"):
        run(["tar", "xvfz", GIT_LFS_TAR_BALL, "git-lfs"])
        run(["cp", "git-lfs", RTD_BIN_DIRECTORY])
        run(["git-lfs", "install"])
        run(["git-lfs", "fetch"])
        run(["git-lfs", "checkout"])


project = "Nissan Leaf OBD-II manual"
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


exclude_patterns = [
    "code/*",
    "includes/*",
]
extensions = [
    "sphinx_rtd_theme",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.spelling",
]
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
