---
published: true
title: 'vixargs: vi[sual] xargs'
layout: post
categories: [projects]
permalink: vixargs-visual-xargs
---

Ever wanted to glance at what your [`xargs`](https://en.wikipedia.org/wiki/Xargs) call is doing? and maybe [show off a little?](https://github.com/dustinkirkland/hollywood)

One more step closer to making the invisible palpable!

*Player seems out of frame and/or text looks squashed? Please head [over here](https://asciinema.org/a/461227).*

<script id="asciicast-461227" src="https://asciinema.org/a/461227.js" async data-autoplay="true" data-loop="true" data-idleTimeLimit="1" data-theme="monokai" data-size="small"></script>

Get the code [here](https://github.com/fenollp/vixargs).

```shell
# Install with:
sudo apt install -y tmux
cargo install --git https://github.com/fenollp/vixargs

# Say the file ./commands has one shell command per line
vixargs -a commands.txt
```
