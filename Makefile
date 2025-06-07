# These variables may be set from the command line, and also from the
# environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# First so that "make" without arguments is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.PHONY: install-git-hooks
install-git-hooks:
	git config --local core.hooksPath 'git-hooks'

.PHONY: install-ide-config
install-ide-config:
	rsync --recursive ide-config/ .
	cp source/wordlist.txt .vscode/spellright.dict

.PHONY: lint
lint: lint-python

.PHONY: lint-python
lint-python:
	./$@.sh

# Catch-all target
# route all unknown targets to Sphinx using the "make mode" option. $(O) is a
# shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
