---
published: true
title: Docker, BuildKit & DOCKER_HOST
layout: post
categories: [powerful-concepts, projects, probable-SaaS]
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
DOCKER_BUILDKIT=1 docker build --platform=local -o . git://github.com/docker/buildx
```
This one-liner builds an executable for the current machine from a git repo.

Yes, one can also [pull Dockerfiles from Git repositories](https://docs.docker.com/engine/reference/commandline/build/#git-repositories)!

```shell
# DOCKER_BUILDKIT=1 docker build --platform=local -o . git://github.com/docker/buildx
[+] Building 58.8s (15/15) FINISHED
 => [internal] load git source git://github.com/docker/buildx                                                                                                                            4.4s
 => resolve image config for docker.io/docker/dockerfile:1.2                                                                                                                             1.0s
 => CACHED docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc                                                        0.0s
 => [internal] load git source git://github.com/docker/buildx                                                                                                                            0.3s
 => [internal] load metadata for docker.io/library/golang:1.16-alpine                                                                                                                    1.0s
 => [internal] load metadata for docker.io/tonistiigi/xx:golang@sha256:6f7d999551dd471b58f70716754290495690efa8421e0a1fcf18eb11d0c0a537                                                  0.0s
 => [xgo 1/1] FROM docker.io/tonistiigi/xx:golang@sha256:6f7d999551dd471b58f70716754290495690efa8421e0a1fcf18eb11d0c0a537                                                                1.0s
 => => resolve docker.io/tonistiigi/xx:golang@sha256:6f7d999551dd471b58f70716754290495690efa8421e0a1fcf18eb11d0c0a537                                                                    0.0s
 => => sha256:6f7d999551dd471b58f70716754290495690efa8421e0a1fcf18eb11d0c0a537 3.29kB / 3.29kB                                                                                           0.0s
 => => sha256:3265075f008d7c003eea3e5c4da277cd5049c0aa31d39d1ec35272168f8bf9dd 523B / 523B                                                                                               0.0s
 => => sha256:ebffcbb79133382ea62829f690a0273304a3f4d83cd4876b58af645356512348 466B / 466B                                                                                               0.0s
 => => sha256:a104d17248520be6cb06ad88875c391c27c5e9e2a7f474d8ad6222d6bbe02445 616B / 616B                                                                                               0.4s
 => => extracting sha256:a104d17248520be6cb06ad88875c391c27c5e9e2a7f474d8ad6222d6bbe02445                                                                                                0.0s
 => [gobase 1/4] FROM docker.io/library/golang:1.16-alpine@sha256:3411aef9ae9cb0fe3534fe2a4d1a9745d952d9a5ed1e20a11ff10549731156e8                                                      11.8s
 => => resolve docker.io/library/golang:1.16-alpine@sha256:3411aef9ae9cb0fe3534fe2a4d1a9745d952d9a5ed1e20a11ff10549731156e8                                                              0.0s
 => => sha256:ba3557a56b150f9b813f9d02274d62914fd8fce120dd374d9ee17b87cf1d277d 2.81MB / 2.81MB                                                                                           0.5s
 => => sha256:448433d692de67fadc3e270369294f10bbc32683e28e4144e7d2d2fedbf60756 281.27kB / 281.27kB                                                                                       0.5s
 => => sha256:7c2a3d42746fcfc7f036d78c91f23a708eccc332efd705161238e6aafc5535a9 153B / 153B                                                                                               0.3s
 => => sha256:3411aef9ae9cb0fe3534fe2a4d1a9745d952d9a5ed1e20a11ff10549731156e8 1.65kB / 1.65kB                                                                                           0.0s
 => => sha256:12d5f94cd4d2840e538e82e26a5dfddf711b30cc98a9f6e01bcf65d7aaf7ccd8 1.36kB / 1.36kB                                                                                           0.0s
 => => sha256:19b59f0222410f71faae89932a13c75635f147de093c7a014931f50576e486cd 5.18kB / 5.18kB                                                                                           0.0s
 => => sha256:f6d283d788a6f5f59325116bda7d61102a1bc7f74d902d617ed62cf90c58fdc6 105.69MB / 105.69MB                                                                                       8.6s
 => => extracting sha256:ba3557a56b150f9b813f9d02274d62914fd8fce120dd374d9ee17b87cf1d277d                                                                                                0.1s
 => => sha256:757f90a0dc844e1ca0ce652556adf5fddaaab3b13d949b52fc384525af8c894e 156B / 156B                                                                                               0.7s
 => => extracting sha256:448433d692de67fadc3e270369294f10bbc32683e28e4144e7d2d2fedbf60756                                                                                                0.1s
 => => extracting sha256:7c2a3d42746fcfc7f036d78c91f23a708eccc332efd705161238e6aafc5535a9                                                                                                0.0s
 => => extracting sha256:f6d283d788a6f5f59325116bda7d61102a1bc7f74d902d617ed62cf90c58fdc6                                                                                                2.2s
 => => extracting sha256:757f90a0dc844e1ca0ce652556adf5fddaaab3b13d949b52fc384525af8c894e                                                                                                0.0s
 => [gobase 2/4] COPY --from=xgo / /                                                                                                                                                     0.8s
 => [gobase 3/4] RUN apk add --no-cache file git                                                                                                                                         2.2s
 => [gobase 4/4] WORKDIR /src                                                                                                                                                            0.1s
 => [buildx-version 1/1] RUN --mount=target=.   PKG=github.com/docker/buildx VERSION=$(git describe --match 'v[0-9]*' --dirty='.m' --always --tags) REVISION=$(git rev-parse HEAD)$(if   0.6s
 => [buildx-build 1/1] RUN --mount=target=. --mount=target=/root/.cache,type=cache   --mount=target=/go/pkg/mod,type=cache   --mount=source=/tmp/.ldflags,target=/tmp/.ldflags,from=bu  35.4s
 => [binaries-unix 1/1] COPY --from=buildx-build /usr/bin/buildx /                                                                                                                       0.2s
 => exporting to client                                                                                                                                                                  0.3s
 => => copying files 57.09MB                                                                                                                                                             0.3s
# sha256sum buildx
c941337da6bf9503645e63cd6648b2ee97ae4e0d312faf40473446a05b27d539  buildx
```

This alone is very powerful to me: I see a safe (rootless) and simple (one liner) way for anyone to build and use Open Source Software.

## `DOCKER_HOST`

Let's keep the MindBlowers coming.

`DOCKER_HOST=ssh://othermachine docker ps` lists containers on `othermachine`. (Say you have defined a host `othermachine` in your `~/.ssh/ssh-config`).

YES you can build images or files, with a *local or remote context / Dockerfile* **on a machine with more oomph!**

```shell
# DOCKER_HOST=ssh://othermachine DOCKER_BUILDKIT=1 docker build --platform=local -o . git://github.com/docker/buildx
[+] Building 3.4s (15/15) FINISHED
 => CACHED [internal] load git source git://github.com/docker/buildx                                                                                                                     0.0s
 => resolve image config for docker.io/docker/dockerfile:1.2                                                                                                                             0.8s
 => CACHED docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc                                                        0.0s
 => [internal] load git source git://github.com/docker/buildx                                                                                                                            0.4s
 => [internal] load metadata for docker.io/tonistiigi/xx:golang@sha256:6f7d999551dd471b58f70716754290495690efa8421e0a1fcf18eb11d0c0a537                                                  0.0s
 => [internal] load metadata for docker.io/library/golang:1.16-alpine                                                                                                                    0.3s
 => [xgo 1/1] FROM docker.io/tonistiigi/xx:golang@sha256:6f7d999551dd471b58f70716754290495690efa8421e0a1fcf18eb11d0c0a537                                                                0.0s
 => [gobase 1/4] FROM docker.io/library/golang:1.16-alpine@sha256:3411aef9ae9cb0fe3534fe2a4d1a9745d952d9a5ed1e20a11ff10549731156e8                                                       0.0s
 => CACHED [gobase 2/4] COPY --from=xgo / /                                                                                                                                              0.0s
 => CACHED [gobase 3/4] RUN apk add --no-cache file git                                                                                                                                  0.0s
 => CACHED [gobase 4/4] WORKDIR /src                                                                                                                                                     0.0s
 => CACHED [buildx-version 1/1] RUN --mount=target=.   PKG=github.com/docker/buildx VERSION=$(git describe --match 'v[0-9]*' --dirty='.m' --always --tags) REVISION=$(git rev-parse HEA  0.0s
 => CACHED [buildx-build 1/1] RUN --mount=target=. --mount=target=/root/.cache,type=cache   --mount=target=/go/pkg/mod,type=cache   --mount=source=/tmp/.ldflags,target=/tmp/.ldflags,f  0.0s
 => CACHED [binaries-unix 1/1] COPY --from=buildx-build /usr/bin/buildx /                                                                                                                0.0s
 => exporting to client                                                                                                                                                                  1.4s
 => => copying files 57.09MB                                                                                                                                                             1.4s
```

> I cheated though: this does use a beefier machine but I'm only showing the run which used caching best

```shell
# sha256sum buildx
c941337da6bf9503645e63cd6648b2ee97ae4e0d312faf40473446a05b27d539  buildx
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
