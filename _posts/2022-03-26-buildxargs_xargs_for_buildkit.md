---
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

---

For instance here's a script for **concurrent video downloads**:
```shell
#!/bin/bash -eu

[[ $# -eq 0 ]] && echo "Usage: $0  <URL>+" && exit 1

repo=https://github.com/fenollp/dockerhost-tools--yt-dlp.git#main
# TODO: once https://github.com/moby/moby/pull/42968 is in docker-ce:
#repo=https://github.com/fenollp/dockerhost-tools.git#:yt-dlp

commands=''
for ((i=1; i<=$#; i++)); do
    url="${!i}"

    ARGs="$url"
    if [[ "$url" = *youtube* ]]; then
        ARGs="--format mp4 -- $url"
    fi
    commands+=$(printf "docker build --build-arg ARGs='%s' --output=$HOME/ %s" "$ARGs" "$repo")"\n"
done

export DOCKER_HOST=ssh://cdg.oomphr.dev
printf "$commands" | buildxargs
docker builder prune --keep-storage 20000000000 -f
```
