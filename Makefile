PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: html clean serve publish copy-static-html

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	$(MAKE) copy-static-html

clean:
	rm -rf $(OUTPUTDIR)

serve: html
	cd $(OUTPUTDIR) && $(PY) -m http.server 8000

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	$(MAKE) copy-static-html

# Copy standalone HTML pages from content/extra/ to output/.
# Pelican's READERS = {"html": None} setting skips HTML in STATIC_PATHS,
# so these need to be copied manually post-build. Each entry pairs a
# source HTML in content/extra/<dir>/index.html with output/<dir>/index.html.
copy-static-html:
	@for d in brand-review materials-periodic-table hipcamp verizon; do \
		if [ -f $(INPUTDIR)/extra/$$d/index.html ]; then \
			mkdir -p $(OUTPUTDIR)/$$d ; \
			cp $(INPUTDIR)/extra/$$d/index.html $(OUTPUTDIR)/$$d/index.html ; \
			echo "Copied $$d/index.html" ; \
		fi ; \
	done
	@for d in qa-startup-maine-2026-05-18; do \
		if [ -d $(INPUTDIR)/extra/$$d ]; then \
			mkdir -p $(OUTPUTDIR)/$$d ; \
			cp -R $(INPUTDIR)/extra/$$d/. $(OUTPUTDIR)/$$d/ ; \
			echo "Copied $$d/ (recursive)" ; \
		fi ; \
	done
