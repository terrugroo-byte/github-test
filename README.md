# github-test

A tiny sandbox project for practicing Git/GitHub workflows (branches, PRs,
issues, Actions) and for testing how Claude Code can drive `gh` on my behalf.

The app itself is intentionally small: a command-line to-do list.

## Usage

```bash
python todo.py add "buy milk"
python todo.py list
python todo.py done 0
python todo.py rm 0
```

## Tests

```bash
python -m unittest discover tests
```
