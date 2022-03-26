---
published: true
title: 'buildxargs: xargs for BuildKit'
layout: post
categories: [projects, buildkit]
permalink: buildxargs_xargs_for_buildkit
---

A specialization of [`vixargs`](./vixargs-visual-xargs) for `docker build` commands.

Fork [`buildxargs`](https://github.com/fenollp/buildxargs)!

```shell
❯ cargo install --git https://github.com/fenollp/buildxargs

# export DOCKER_HOST=ssh://much.oomphr.dev
❯ buildxargs <<EOF
docker build --build-arg ARGs='--format mp4 -- https://www.youtube.com/watch?v=Hj7LwZqTflc' --output=$HOME https://github.com/fenollp/dockerhost-tools--yt-dlp.git#main
docker build -o=. --platform=local --build-arg PREBUILT=1 https://github.com/FuzzyMonkeyCo/monkey.git
docker build --platform=local -o . https://github.com/docker/buildx.git
EOF
```

<script id="asciicast-tOf28m3MIdDI4IBRE53QAaYG5" src="https://asciinema.org/a/tOf28m3MIdDI4IBRE53QAaYG5.js" async data-autoplay="true" data-loop="true" data-idleTimeLimit="1" data-theme="monokai" data-size="small"></script>

*Player seems out of frame and/or text looks squashed? Please head [over here](https://asciinema.org/a/tOf28m3MIdDI4IBRE53QAaYG5).*
