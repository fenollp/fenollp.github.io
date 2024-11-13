debug:
	mkdir -p _site
	docker run --rm -it \
	  -v "$$PWD":/srv/jekyll:Z \
	  -p 4000:4000 \
	  -e JEKYLL_UID=$$(id -u) \
	  -e JEKYLL_GID=$$(id -g) \
	  -e JEKYLL_ROOTLESS=1 \
	  jekyll/jekyll:4.1.0 \
	  jekyll serve --watch --drafts --trace

new.%:
	touch _posts/$$(date +%F)-$*.md
	echo '---' >>$$(ls _posts/* -t | head -n1)
	echo 'wip: true' >>$$(ls _posts/* -t | head -n1)
	echo "title: $$(echo $* | sed 's%-% %g;s%_% %g')" >>$$(ls _posts/* -t | head -n1)
	echo 'layout: post' >>$$(ls _posts/* -t | head -n1)
	echo 'categories: [projects]' >>$$(ls _posts/* -t | head -n1)
	echo 'permalink: $*' >>$$(ls _posts/* -t | head -n1)
	echo '---' >>$$(ls _posts/* -t | head -n1)
	git add $$(ls _posts/* -t | head -n1)
	$(EDITOR) $$(ls _posts/* -t | head -n1)

clean:
	$(if $(wildcard _site), rm -rf _site || sudo rm -rf _site)
	$(if $(wildcard .jekyll-cache), rm -rf .jekyll-cache || sudo rm -rf .jekyll-cache)
