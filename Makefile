debug:
	docker run --rm -it \
	  -v "$$PWD":/srv/jekyll \
	  -p 4000:4000 \
	  jekyll/jekyll \
	  jekyll serve --watch --drafts

new.%:
	$(EDITOR) _posts/$$(date +%F)-$*.md

clean:
	$(if $(wildcard _site), rm -r _site)
	$(if $(wildcard .jekyll-cache), rm -r .jekyll-cache)
