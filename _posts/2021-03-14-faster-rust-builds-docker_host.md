---
published: true
title: Infinitely faster initial Rust builds with DOCKER_HOST (and BuildKit)
layout: post
categories: [much-wow, trusting-trust, probable-SaaS, Merkle-cache, docker_host, buildkit]
permalink: faster-rust-builds-docker_host
---

Following my first [blog post ever on a similar subject](./docker-buildkit-docker_host) I found [`cargo-wharf`](https://github.com/denzp/cargo-wharf/tree/ef460f80bf8fe1b9ec95dad321a79929d67f0c45), a *cacheable and efficient Docker images builder for Rust*.

This is an [alternate Dockerfile frontend syntax](https://github.com/moby/buildkit/blob/2be23848e889186388b6d422dfb6e9ca2e8d19cb/frontend/dockerfile/docs/syntax.md) implementation for Rust:
it converts a `Cargo.toml` (a file listing `cargo` / Rust dependencies and things) into a `docker build`able recipe by adding this `# syntax` line (+ caveats)
```toml
# syntax = denzp/cargo-wharf-frontend:v0.1.0-alpha.2

[package]
...
```

Then with the following one is able to create a Docker image *from this Cargo.toml*
```shell
$ DOCKER_BUILDKIT=1 docker build -t service:latest -f Cargo.toml .
```

Not demonstrated in that repo but supposedly supported is building binaries:
```shell
$ DOCKER_BUILDKIT=1 docker build --platform=local --output=. --file=Cargo.toml .
# or even:
$ DOCKER_BUILDKIT=1 docker build --platform=local --output=. https://github.com/some/repo.git#master:sub/context
```
> > Note that using Docker context `sub/context` [isn't yet supported by BuildKit](https://github.com/moby/buildkit/issues/1684)...

As noted in that repo's README:
> Every dependency is built in its isolated environment and cached independently from others.

Rust projects are notoriously slow to build, especially the initial build.
* *Incremental builds fast enough for a short dev loop though!*
* using "thin" LTO helps but [build times can still be a hindrance](https://github.com/rust-lang/rust/issues/71850) when using [`cross`](https://github.com/rust-embedded/cross)

Being a fan of `DOCKER_HOST` this immediately tickled my ears!

## A mutualized build artifacts cache

Say you want to work on some large Rust project for the first time. You clone it, then `DOCKER_BUILDKIT=1 docker build --platform=local ...` it having set `DOCKER_HOST=ssh://some_machine.com`.

Now your build runs on a beefy machine somewhere and sends you the outputs.

Not only
* did the build take a fraction of the time it would take on your machine
* but it reaped the benefits of a lightspeed fast connection to the dependency cache!

The Rust community and its backers
* could support such a cache (for example by paying for compute, bandwidth and storage)
* share the hurdle of building dependencies (given specific flags / architecture triplet / `rustc` version / ...)

Unsure your remote-built project wasn't backdoored by a malicious some_machine.com / cache / middle person?
> Unset `DOCKER_HOST`, re-run the command and compare `sha256(remote-built)` with `sha256(locally-built)`

In fact, all language communities should be sharing a build cache, provided
* they often suffer from long build times
* tooling allows for hermetic builds
* they [trust their tools](https://dl.acm.org/doi/10.1145/358198.358210)

I'm obviously not a genius. Here are some of other people's take on this:
* [5x Faster Rust Docker Builds with cargo-chef](https://www.lpalmieri.com/posts/fast-rust-docker-builds/)
	* [A cargo-subcommand to speed up Rust Docker builds using Docker layer caching.](https://github.com/LukeMathWalker/cargo-chef)
	* note how it only caches dependencies, maybe even just the public ones
* [Mozillas's sccache is ccache with cloud storage](https://github.com/mozilla/sccache)
* [Gradle's Build Cache](https://docs.gradle.org/current/userguide/build_cache.html)
	* a (centralized) cache is provided *for money*
		* **Did we just find a[nother] financial incentive to support developer communities?**
* [Nix's Binary Cache](https://nixos.wiki/wiki/Binary_Cache)
	* see also [Cachix](https://cachix.org/)

## private code & security

These are the privacy and security concerns I can see from my echo-chamber-slash-comfy-chair:
* Building non-public code / private dependencies
	* and not contributing back to the build cache
* Not being able to reconstruct a private project from the cache nor how it accesses the cache
* Asserting a given build artifact was not tempered with

To address these points I see:
* Tooling should separate public from private
	* *the tools closer to the language have the best semantics*
	* a private cache should be easy to set up (in any Continuous Integration system)
	* with fallback on the single public cache on misses
* A [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree)
	* [content-addressable storage](https://en.wikipedia.org/wiki/Content-addressable_storage)
	* with granular enough blocks ([Bittorrent v2 says >=16kiB](https://blog.libtorrent.org/2020/09/bittorrent-v2/))
		* *a dependency would be associated its root hash in the tree and resolve to many blocks*
	* with [numerous enough accesses to hide](https://en.wikipedia.org/wiki/Law_of_large_numbers) a single actor's usage
	* [Bazil](https://bazil.org/doc/) seems related, has good security buzzwords
		* it does not seem to be aimed at being a cache (e.g. pruning should be harmless)
* Stochastic re-building / cache pruning
	* should provide a reliable way of [Proof-of-Work](https://en.wikipedia.org/wiki/Proof_of_work)
	* by computing builds multiple times (and achieving the same results)

I'm describing a [DHT](https://en.wikipedia.org/wiki/Distributed_hash_table), a decentralized one. Maybe even [IPFS](https://docs.ipfs.io/concepts/how-ipfs-works).
