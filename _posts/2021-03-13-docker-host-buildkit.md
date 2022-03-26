---
published: true
title: Docker, BuildKit & DOCKER_HOST
layout: post
categories: [powerful-concepts, projects, probable-SaaS, docker_host]
permalink: docker-buildkit-docker_host
---

I recently discovered Docker's [`BuildKit`](https://github.com/moby/buildkit).
I'm a bit late to the party: this [has been part of the `docker` command since version `18.09`](https://docs.docker.com/develop/develop-images/build_enhancements/), probably in the "experimental" features.

In short, `BuildKit` is `DOCKER_BUILDKIT=1 docker build ...`
* building on [multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)
* much more [cache-efficient](https://github.com/moby/buildkit/blob/2be23848e889186388b6d422dfb6e9ca2e8d19cb/frontend/dockerfile/docs/syntax.md#run---mounttypecache) than `docker build` with `RUN --mount=...`
* more compute-efficient as well: graph is topologically sorted and executed concurrently plus the docs talk about distribution
* runs [rootless](https://github.com/moby/buildkit/blob/2be23848e889186388b6d422dfb6e9ca2e8d19cb/docs/rootless.md)!
* build can [`--output` files](https://docs.docker.com/engine/reference/commandline/build/#custom-build-outputs) to `$PWD`!
* `--platform` support with fallback on emulation (uses QEMU)

## An example

I stumbled upon `BuildKit` when checking out [`buildx`](https://github.com/docker/buildx). The suggested way of building the executable caught my eye:
```shell
DOCKER_BUILDKIT=1 docker build --platform=local -o . https://github.com/docker/buildx.git
```
This one-liner builds an executable for the current machine from a git repo.

Yes, one can also [pull Dockerfiles from Git repositories](https://docs.docker.com/engine/reference/commandline/build/#git-repositories)!

```shell
❯ DOCKER_BUILDKIT=1 docker build --platform=local -o . https://github.com/docker/buildx.git
[+] Building 65.1s (17/17) FINISHED                                                                                                                                                           
 => [internal] load git source https://github.com/docker/buildx.git                                                                                                                      4.4s
 => resolve image config for docker.io/docker/dockerfile:1.3                                                                                                                             1.1s 
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                                                                                                                         0.0s 
 => CACHED docker-image://docker.io/docker/dockerfile:1.3@sha256:42399d4635eddd7a9b8a24be879d2f9a930d0ed040a61324cfdf59ef1357b3b2                                                        0.0s 
 => [internal] load metadata for docker.io/library/golang:1.17-alpine                                                                                                                    1.5s 
 => [internal] load metadata for docker.io/tonistiigi/xx:1.0.0                                                                                                                           1.5s 
 => [auth] library/golang:pull token for registry-1.docker.io                                                                                                                            0.0s 
 => [auth] tonistiigi/xx:pull token for registry-1.docker.io                                                                                                                             0.0s
 => [xx 1/1] FROM docker.io/tonistiigi/xx:1.0.0@sha256:494fa8488689d499edfaa16dba5922bc2b8cdfcb220bf884354aecbc1f2d8996                                                                  0.9s
 => => resolve docker.io/tonistiigi/xx:1.0.0@sha256:494fa8488689d499edfaa16dba5922bc2b8cdfcb220bf884354aecbc1f2d8996                                                                     0.0s
 => => sha256:494fa8488689d499edfaa16dba5922bc2b8cdfcb220bf884354aecbc1f2d8996 2.65kB / 2.65kB                                                                                           0.0s
 => => sha256:c175b0065054f5c2285c727510f433231f8ebe41d437816d22044696e9adde44 525B / 525B                                                                                               0.0s
 => => sha256:0f3509935530631c6c402f33310ff23d7bd35caf9ba63059d4157c39329a10d4 940B / 940B                                                                                               0.0s
 => => sha256:25eaaac5d58a9b6ff4e90ee3cbd4149fd0861e2605d3d11c64e265ba5ba45176 13.99kB / 13.99kB                                                                                         0.7s
 => => extracting sha256:25eaaac5d58a9b6ff4e90ee3cbd4149fd0861e2605d3d11c64e265ba5ba45176                                                                                                0.0s
 => [golatest 1/1] FROM docker.io/library/golang:1.17-alpine@sha256:b48997f9a0479c9707298621acbcccb9158eb46c091d5123ae65ce5e791fa2cf                                                    10.6s
 => => resolve docker.io/library/golang:1.17-alpine@sha256:b48997f9a0479c9707298621acbcccb9158eb46c091d5123ae65ce5e791fa2cf                                                              0.0s
 => => sha256:b48997f9a0479c9707298621acbcccb9158eb46c091d5123ae65ce5e791fa2cf 1.65kB / 1.65kB                                                                                           0.0s
 => => sha256:f4ece20984a30d1065b04653bf6781f51ab63421b4b8f011565de0401cfe58d7 1.36kB / 1.36kB                                                                                           0.0s
 => => sha256:6557bff276fa9485ad7f498c7eded89730e526c2a70fb8c399375c6cd27d9640 5.17kB / 5.17kB                                                                                           0.0s
 => => sha256:3aa4d0bbde192bfaba75f2d124d8cf2e6de452ae03e55d54105e46b06eb8127e 2.81MB / 2.81MB                                                                                           0.3s
 => => sha256:48ae170c2a8ceb6dfe7dd52edb58d7be5583518415f0e441c5b7d4f0f8bad244 271.97kB / 271.97kB                                                                                       0.5s
 => => sha256:cb35b180f41941e8ec9af85110ff412f204e4afaf593ac8fc601c07b7449304d 154B / 154B                                                                                               0.5s
 => => extracting sha256:3aa4d0bbde192bfaba75f2d124d8cf2e6de452ae03e55d54105e46b06eb8127e                                                                                                0.1s
 => => sha256:367011ddbc177b50e507d24a640d8fdbdd64a32a4b0e2a3549ad26a1c0581da5 110.19MB / 110.19MB                                                                                       6.9s
 => => extracting sha256:48ae170c2a8ceb6dfe7dd52edb58d7be5583518415f0e441c5b7d4f0f8bad244                                                                                                0.1s
 => => sha256:318840287a8912b4d3a5caf13e21932dd668cfa441f84c3f7cb89884f12bc498 155B / 155B                                                                                               0.7s
 => => extracting sha256:cb35b180f41941e8ec9af85110ff412f204e4afaf593ac8fc601c07b7449304d                                                                                                0.0s
 => => extracting sha256:367011ddbc177b50e507d24a640d8fdbdd64a32a4b0e2a3549ad26a1c0581da5                                                                                                3.1s
 => => extracting sha256:318840287a8912b4d3a5caf13e21932dd668cfa441f84c3f7cb89884f12bc498                                                                                                0.0s
 => [gobase 1/3] COPY --from=xx / /                                                                                                                                                      0.8s
 => [gobase 2/3] RUN apk add --no-cache file git                                                                                                                                         1.7s
 => [gobase 3/3] WORKDIR /src                                                                                                                                                            0.0s 
 => [buildx-version 1/1] RUN --mount=target=.   PKG=github.com/docker/buildx VERSION=$(git describe --match 'v[0-9]*' --dirty='.m' --always --tags) REVISION=$(git rev-parse HEAD)$(if   0.4s 
 => [buildx-build 1/1] RUN --mount=type=bind,target=.   --mount=type=cache,target=/root/.cache   --mount=type=cache,target=/go/pkg/mod   --mount=type=bind,source=/tmp/.ldflags,target  43.2s 
 => [binaries-unix 1/1] COPY --from=buildx-build /usr/bin/buildx /                                                                                                                       0.2s 
 => exporting to client                                                                                                                                                                  0.3s 
 => => copying files 47.80MB                                                                                                                                                             0.3s 
❯ sha256sum buildx
693a6128fb1ad5c7c598a02599111690f8ec89d6d24c3d86b59dd64286edb931  ./buildx
```

This alone is very powerful to me: I see a safe (rootless) and simple (one liner) way for anyone to build and use Open Source Software.

## `$DOCKER_HOST`

Let's keep the MindBlowers coming.

`DOCKER_HOST=ssh://othermachine docker ps` lists containers on `othermachine`. (Say you have defined a host `othermachine` in your `~/.ssh/ssh-config`).

YES you can build images or files, with a *local or remote context / Dockerfile* **on a machine with more oomph!**

```shell
❯ DOCKER_HOST=ssh://othermachine DOCKER_BUILDKIT=1 docker build --platform=local -o . https://github.com/docker/buildx.git
[+] Building 3.7s (17/17) FINISHED                                                                                                                                                            
 => CACHED [internal] load git source https://github.com/docker/buildx.git                                                                                                               0.5s
 => resolve image config for docker.io/docker/dockerfile:1.3                                                                                                                             0.9s
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                                                                                                                         0.0s
 => docker-image://docker.io/docker/dockerfile:1.3@sha256:42399d4635eddd7a9b8a24be879d2f9a930d0ed040a61324cfdf59ef1357b3b2                                                               0.0s
 => [internal] load metadata for docker.io/library/golang:1.17-alpine                                                                                                                    0.8s
 => [internal] load metadata for docker.io/tonistiigi/xx:1.0.0                                                                                                                           0.6s
 => [auth] tonistiigi/xx:pull token for registry-1.docker.io                                                                                                                             0.0s
 => [auth] library/golang:pull token for registry-1.docker.io                                                                                                                            0.0s
 => [xx 1/1] FROM docker.io/tonistiigi/xx:1.0.0@sha256:494fa8488689d499edfaa16dba5922bc2b8cdfcb220bf884354aecbc1f2d8996                                                                  0.0s
 => [golatest 1/1] FROM docker.io/library/golang:1.17-alpine@sha256:b48997f9a0479c9707298621acbcccb9158eb46c091d5123ae65ce5e791fa2cf                                                     0.0s
 => CACHED [gobase 1/3] COPY --from=xx / /                                                                                                                                               0.0s
 => CACHED [gobase 2/3] RUN apk add --no-cache file git                                                                                                                                  0.0s
 => CACHED [gobase 3/3] WORKDIR /src                                                                                                                                                     0.0s
 => CACHED [buildx-version 1/1] RUN --mount=target=.   PKG=github.com/docker/buildx VERSION=$(git describe --match 'v[0-9]*' --dirty='.m' --always --tags) REVISION=$(git rev-parse HEA  0.0s
 => CACHED [buildx-build 1/1] RUN --mount=type=bind,target=.   --mount=type=cache,target=/root/.cache   --mount=type=cache,target=/go/pkg/mod   --mount=type=bind,source=/tmp/.ldflags,  0.0s
 => CACHED [binaries-unix 1/1] COPY --from=buildx-build /usr/bin/buildx /                                                                                                                0.0s
 => exporting to client                                                                                                                                                                  1.2s
 => => copying files 47.80MB                                                                                                                                                             1.2s
```

> I cheated though: this does use a beefier machine but I'm only showing the run which used caching best

```shell
❯ sha256sum buildx
693a6128fb1ad5c7c598a02599111690f8ec89d6d24c3d86b59dd64286edb931  ./buildx
```

And, if you are careful enough or you're given the right tools, you should achieve [hermetic / deterministic / reproducible builds](https://reproducible-builds.org/)!
IMO this is a tooling problem and Dockerfiles need a lockfile (other [Dockerfile syntaxes](https://blog.libtorrent.org/2020/09/bittorrent-v2/) don't seem to aim this way though).
BTW here's a [lockfile system I built for Bazel](https://github.com/fenollp/bazel_upgradable) and that should be a stepping stone for a *universal lockfile* thing, but more on this later.

## `DOCKER_HOST` ~ a potential business idea

Here's the SaaS idea:
* Sell compute that's accessible only via `DOCKER_HOST + docker build`
* that is instantly usable (queuing more than the half life of the job should be an error)
* that outputs only files (building images is another business)
* uses
	* users can turn their build command into a *distributed* one [with one simple trick!]
	* dev tooling (linters, ...) with context=$PWD and dockerfile=$LIB_ON_GIT/Dockerfile.$TOOL
	* convert CI workflows
		* => "local" troubleshooting
		* => CI providers are to be eaten by this very business idea
	* reproducible builds (strong incentive via execution times and caching)
	* any-platform distribution
	* *this is time-sharing*
	* this is NOT "like deploying images with k8s"
		* this is maybe exactly **k8s jobs** though
	* this is cron with RCE
	* > run AI model on latest videos uploaded in parallel for recommendation system
	* this is map/reduce pr0n without error handling strategies
	* > regen the map of this game you're building. It uses a picture of the Earth by NASA and eats 100% CPU of your laptop for like 2h. Your script is ready to eat x10 cores so as to finish only in 12min.
	* this is a safe `curl https://get.my.app | bash` and [soon] as-portable
	* faster builds for Apple Silicon (or just Apple) owners: saves cost of emulation
* the compute can be tuned on the website
	* where one can select & name machines
	* add/remove SSH credentials
	* can buy more minutes
	* future: HW auto-up/down-grade (e.g. ex terminal.com)
	* pay to maintain N>=0 in your pools
	* distribution slider [0->M makes M-1 dependencies run on M-1 other machines
	* shared cache as blob storage [wink wink Bittorrent v2](https://blog.libtorrent.org/2020/09/bittorrent-v2/)
* flow
	* SSH connection comes in
	* keyphrase already validated
	* let's find an account/machine matching user / password / keyphrase / sub-tld of the SSH URI DOCKER_HOST=ssh://user@token:saas.com/machine0
	* let's verify we're building `--output` files
	* let's verify we're not opening ports
	* let's verify we're rootless
	* hand off to `buildkitd` running on the configured machine
		* with a deadline

## misc

Build a [specific multi-stage image](https://docs.docker.com/engine/reference/commandline/build/#specifying-target-build-stage---target). See more about this with [`docker buildx build bake`](https://docs.docker.com/engine/reference/commandline/buildx_bake/) and a [telling example](https://github.com/goreleaser/goreleaser-action/pull/258/files?file-filters%5B%5D=.dev&file-filters%5B%5D=.hcl&file-filters%5B%5D=.md&file-filters%5B%5D=.yml&hide-deleted-files=true).

You can [`RUN --network=none ...`](https://github.com/moby/buildkit/blob/2be23848e889186388b6d422dfb6e9ca2e8d19cb/frontend/dockerfile/docs/syntax.md#example-isolating-external-effects) so your command cannot access Internet!

I've adapted [`buildx`'s Dockerfile](https://github.com/docker/buildx/blob/c9f02c32d495e364894b6f128594fb6f72991312/Dockerfile) for "easy" install of my [`monkey`](https://github.com/FuzzyMonkeyCo/monkey/pull/104)

Closing thought / home assignment: what can `BuildKit` bring to [`whalebrew`](https://github.com/whalebrew/whalebrew)?
