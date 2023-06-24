# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
TMP_DIR       = /tmp/opencdms-docs-gh-pages

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

deploy:
	mkdir -p $(TMP_DIR)
	git clone -b gh-pages https://github.com/opencdms/opencdms $(TMP_DIR) --depth=1
	# Delete everything on the gh-pages branch except for the git history (.git)
	find $(TMP_DIR) -not -path '*/\.git/*' -delete
	sphinx-build -b html source $(TMP_DIR)

	cd $(TMP_DIR)
	git add .
	git commit -m "Update docs and deploy"
	git push origin gh-pages && rm -rf $(TMP_DIR)
