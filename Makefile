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
install-git-hooks: .git/hooks/pre-commit

.git/hooks/%: git-hooks/%.sh
	install --mode=700 $< $@

.PHONY: install-ide-config
install-ide-config:
	rsync --recursive ide-config/ .
	cp source/wordlist.txt .vscode/spellright.dict

.PHONY: install-vale-styles
install-vale-styles:
	rm -rf styles/Google
	curl -sL https://github.com/errata-ai/Google/archive/v0.3.1.tar.gz \
	| tar zxf - -C styles/ --strip-components=1 Google-0.3.1/Google

.PHONY: lint
lint: lint-prose

.PHONY: lint-prose
lint-prose:
	./$@.sh

# Catch-all target
# route all unknown targets to Sphinx using the "make mode" option. $(O) is a
# shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
