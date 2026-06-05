PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: html clean serve publish copy-static-html llms-full

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	$(MAKE) copy-static-html
	$(MAKE) llms-full

clean:
	rm -rf $(OUTPUTDIR)

serve: html
	cd $(OUTPUTDIR) && $(PY) -m http.server 8000

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	$(MAKE) copy-static-html
	$(MAKE) llms-full

# Generate output/llms-full.txt (full-text concatenation for AI agents) from the
# freshly-built output. Runs after pelican + copy-static-html on every build.
llms-full:
	$(PY) tools/build_llms_full.py

# Copy standalone HTML pages from content/extra/ to output/.
# Pelican's READERS = {"html": None} setting skips HTML in STATIC_PATHS,
# so these need to be copied manually post-build. Each entry pairs a
# source HTML in content/extra/<dir>/index.html with output/<dir>/index.html.
copy-static-html:
	@for d in brand-review materials-periodic-table hipcamp verizon towers discussion-our-katahdin-2026-05-28 discussion-desri-svedlow discussion-desri-nicc-johnson discussion-oskar-serrander-2026-06-01 discussion-ready-net discussion-kite-realty discussion-new-leaf-energy discussion-ac-power discussion-ct-mirror discussion-verogy discussion-cianbro overview-v4; do \
		if [ -f $(INPUTDIR)/extra/$$d/index.html ]; then \
			mkdir -p $(OUTPUTDIR)/$$d ; \
			cp $(INPUTDIR)/extra/$$d/index.html $(OUTPUTDIR)/$$d/index.html ; \
			echo "Copied $$d/index.html" ; \
		fi ; \
	done
	@for d in qa-startup-maine-2026-05-18 ai-in-action; do \
		if [ -d $(INPUTDIR)/extra/$$d ]; then \
			mkdir -p $(OUTPUTDIR)/$$d ; \
			cp -R $(INPUTDIR)/extra/$$d/. $(OUTPUTDIR)/$$d/ ; \
			echo "Copied $$d/ (recursive)" ; \
		fi ; \
	done
