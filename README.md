# Harness Creator

Harness Creator helps users define agent harnesses through a guided conversation.

## Current scope

This initial version accepts a natural-language harness description. It does not create harness files, save request data to disk, or send request data to an external service.

## Requirements

- Python 3.14 or later
- [uv](https://docs.astral.sh/uv/)

## Run

```sh
uv run harness-creator
```

The application asks for one harness description. Enter a non-empty description to continue, or press `Ctrl-D` / `Ctrl-C` to exit.

## Run tests

```sh
uv run python -m unittest discover -s tests
```