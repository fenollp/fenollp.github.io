debug:
	docker run --rm -it \
	  -v "$$PWD":/srv/jekyll \
	  -p 3000:4000 \
	  jekyll/jekyll \
	  jekyll serve --watch --drafts
