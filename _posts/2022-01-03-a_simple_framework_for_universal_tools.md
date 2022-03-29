---
title: A simple framework for universal tools
layout: post
categories: [projects, docker_host, buildkit, golang]
permalink: a_simple_framework_for_universal_tools
---

I have discussed on this blog the interesting property of Docker BuildKit: a portable shell executor that can even run remotely, similarly to the serverless buzzword^Wthing.

However there's an issue that's been bugging me.
I want developer tools based on `docker build` such as a file formatter or `protoc` a [Protocol Buffers compiler](https://developers.google.com/protocol-buffers) (have a look [here](https://buf.build/) on this specific subject) or anything else really, especially if the tool would run faster on a bigger machine with large caching!

The Docker `build` command as is requires some more code around just to pipe files into and out of the `build`, through the right tool and to the right filesystem places.

Anyhow, the command accepts a TAR-ed Dockerfile and context on STDIN and can output a TAR on STDOUT. So, I wrote some code that's strict on its inputs.

> Be very strict on what inputs your programs accept, this will give you a stable basis to build on and more freedom of movement.

## lib: [`github.com/fenollp/fmtd/buildx`](https://pkg.go.dev/github.com/fenollp/fmtd/buildx)


See for yourself [over here](https://github.com/fenollp/fmtd/blob/35b13910c2e067551eb8980e99a82afb6f037e5c/buildx/buildx.go), but here's the meat of it:

```go
	// ...

	tw := tar.NewWriter(&stdin)
	{
		hdr := &tar.Header{
			Name: "Dockerfile",
			Mode: 0200,
			Size: int64(len(dockerfile)),
		}
		if err := tw.WriteHeader(hdr); err != nil {
			return err
		}
		if _, err := tw.Write(dockerfile); err != nil {
			return err
		}
	}
	for _, ifile := range o.ifiles {
		// ...
	}
	if err := tw.Close(); err != nil {
		return err
	}

	o.args = append(o.args, "-")
	cmd := exec.CommandContext(o.ctx, o.exe, o.args...)
	cmd.Env = append(o.env, "DOCKER_BUILDKIT=1")
	cmd.Stdin = &stdin
	var tarbuf bytes.Buffer
	cmd.Stdout = &tarbuf
	cmd.Stderr = o.stderr
	if err := cmd.Run(); err != nil {
		return err
	}

	tr := tar.NewReader(&tarbuf)
	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			break // End of archive
		}
		if err != nil {
			return err
		}
		// ...
	}

	// ...
}
```
It creates a tar archive with Dockerfile and context, then passes it to an `os/exec` command instance and finally reads the tar archive being outputted on that command's stdout slot.
Nothing fancy, really most of the code here is to try to give a nice composable API on top of fingers-crossed strict enough input handling.

Oh and I tried relying on the [Go Docker client](https://github.com/moby/moby) but could not make it support the `DOCKER_HOST` env so this relies on the docker command... *please send help.*


## Example: `fmtd` ~ universal formatter

This is a tiny program that uses the above library and reformats various files: Go, C++, Protobuf, JSON, SQL and more.

Install with: (yes, it installs with Docker then runs with Docker, dawg!)

```shell
export DOCKER_BUILDKIT=1
docker build -o=/usr/local/bin/ https://github.com/fenollp/fmtd.git#main
```

Run with

```shell
λ fmtd setup*
setup.py
setup_android_sdk_and_ndk.sh
setup_opencv.sh
```

Here's an alias to reformat Git tracked and cached files:
```shell
gfmt() {
    while read -r f; do
        fmtd "$f"
    done < <(git status --short --porcelain -- . | \grep '^. ' | \grep -Eo '[^ ]+$')
}
```

Next I'll publish a `protoc` tool using this technique.

Hermetic versioning and a networked cache should make for a simplest-to-install and fast protobuf compiler.
