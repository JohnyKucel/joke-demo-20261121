# The joke about the demo

A make.fun bounty entry: a one-line joke about working beside an AI coding
agent during a live software demo — the rehearsal went fine, the live demo
did not, and the agent stayed confident throughout.

## How it works

`main.py` is a small Python 3.13 program that uses only the standard library.
It writes the joke, plus a trailing newline, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable (falling
back to `/output`). It is deterministic: no network access, no randomness,
no clock.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/demo-output python3 main.py
cat /tmp/demo-output/entry.txt
```

## License

MIT — see `LICENSE`.
