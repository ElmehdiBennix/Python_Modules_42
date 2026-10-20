# Module 1 — Array

*Training Piscine Python for Data Science — Module 1: Array*
**Array manipulation and working with images**

This module introduces NumPy arrays and applies them to real data: computing a BMI
from lists of measurements, slicing 2D tables, loading images as arrays, cropping,
transposing and applying colour filters.

---

## Requirements

| | |
|---|---|
| **Python** | 3.10 (pinned in `.python-version`) |
| **Package manager** | [uv](https://docs.astral.sh/uv/) |
| **Libraries** | `numpy`, `pillow`, `matplotlib` (+ `flake8`, `black` for development) |

## Setup

```bash
uv sync          # or: make install
```

This creates `.venv/` with every dependency and installs the `norminette` command
(see [Code norm](#code-norm)).

---

## Project structure

```
Module_1/
├── Doc/                   # Reference documentation, one file per exercise
│   ├── ex00.md
│   ├── ex01.md
│   ├── ex02.md
│   ├── ex03.md
│   ├── ex04.md
│   └── ex05.md
├── ex00/                  # Exercise 00 — Give my BMI
│   ├── give_bmi.py        #   deliverable
│   └── tester.py          #   test program
├── ex01/                  # Exercise 01 — 2D array
│   ├── array2D.py         #   deliverable
│   └── tester.py
├── ex02/                  # Exercise 02 — Load my image
│   ├── load_image.py      #   deliverable
│   └── tester.py
├── ex03/                  # Exercise 03 — Zoom on me
│   ├── load_image.py      #   deliverable
│   └── zoom.py            #   deliverable
├── ex04/                  # Exercise 04 — Rotate me
│   ├── load_image.py      #   deliverable
│   └── rotate.py          #   deliverable
├── ex05/                  # Exercise 05 — Pimp my image
│   ├── load_image.py      #   deliverable
│   ├── pimp_image.py      #   deliverable
│   └── tester.py
├── subject/               # The subject PDF and the test images
│   ├── en.subject.pdf
│   ├── animal.jpeg        #   768 x 1024 px
│   └── landscape.jpg      #   257 x 450 px
├── .flake8                # flake8 configuration
├── Makefile               # Task runner
├── pyproject.toml         # Project metadata and dependencies
└── uv.lock                # Locked dependency versions
```

---

## Documentation

Each exercise has a companion document in [`Doc/`](Doc/). They cover the subject
requirements, every concept involved, a walkthrough of the implementation, how to
run it, and the key takeaways.

| Exercise | Topic | Document | Deliverable(s) |
|---|---|---|---|
| 00 | Give my BMI | [`Doc/ex00.md`](Doc/ex00.md) | `ex00/give_bmi.py` |
| 01 | 2D array | [`Doc/ex01.md`](Doc/ex01.md) | `ex01/array2D.py` |
| 02 | Load my image | [`Doc/ex02.md`](Doc/ex02.md) | `ex02/load_image.py` |
| 03 | Zoom on me | [`Doc/ex03.md`](Doc/ex03.md) | `ex03/load_image.py`, `ex03/zoom.py` |
| 04 | Rotate me | [`Doc/ex04.md`](Doc/ex04.md) | `ex04/load_image.py`, `ex04/rotate.py` |
| 05 | Pimp my image | [`Doc/ex05.md`](Doc/ex05.md) | `ex05/load_image.py`, `ex05/pimp_image.py` |

---

## Running the exercises

Each exercise is a standalone program. **Run it from inside its own directory**,
because the image paths are relative to the working directory.

```bash
cd ex00 && ../.venv/bin/python tester.py
cd ex01 && ../.venv/bin/python tester.py
cd ex02 && ../.venv/bin/python tester.py
cd ex03 && ../.venv/bin/python zoom.py
cd ex04 && ../.venv/bin/python rotate.py
cd ex05 && ../.venv/bin/python tester.py
```

With the virtual environment activated (`make activate`), `python tester.py` works
directly.

> **Headless machines** — `ex03`, `ex04` and `ex05` open Matplotlib windows. On a
> server without a display, force a non-interactive backend:
> `MPLBACKEND=Agg python zoom.py`.

---

## Make targets

| Target | Description |
|---|---|
| `make help` | List all available targets |
| `make install` | Sync the virtual environment (`uv sync`) |
| `make activate` | Activate the virtual environment |
| `make test` | Run the tester of every exercise |
| `make lint` | Check the code norm (flake8) |
| `make norminette` | Alias of `make lint` |
| `make format` | Format the code with black (79 characters, norm compatible) |
| `make clean` | Remove the Python caches |
| `make fclean` | Remove the caches and the virtual environment |

```bash
make test
#   ex00   tester.py    OK
#   ex01   tester.py    OK
#   ex02   tester.py    OK
#   ex03   zoom.py      OK
#   ex04   rotate.py    OK
#   ex05   tester.py    OK
#   All testers passed.
```

---

## Code norm

The subject requires the code to follow the 42 norm, which is `flake8` under the name
`norminette`. The alias is declared in `pyproject.toml` as a project script:

```toml
[project.scripts]
norminette = "flake8.main.cli:main"
```

It is therefore available directly from the virtual environment:

```bash
uv run norminette .        # or: make lint
uv run norminette --version
```

The `.flake8` configuration excludes `.venv`, `.git` and the Python caches, and sets
the maximum line length to 79 characters. Without that exclusion, `flake8 .` would
report tens of thousands of issues coming from the installed libraries.

`make format` runs `black` with a line length of 79, which stays compatible with
`flake8`.

---

## Subject requirements

The following rules apply to every exercise of the module and are enforced
throughout the implementation:

* No code in the global scope — everything lives in functions.
* Every program has a `main()` function and the `if __name__ == "__main__":` guard.
* Every function has a docstring (`__doc__`).
* No global variables.
* Explicit imports only (`import numpy as np`); wildcard imports are forbidden.
* Every exception is caught and reported with a clear message.
* The code is `flake8` clean (the 42 norm).

The full subject is available in [`subject/en.subject.pdf`](subject/en.subject.pdf).

---

## Dependencies

| Package | Purpose |
|---|---|
| `numpy` | Arrays, vectorised arithmetic, boolean masks |
| `pillow` | Reading JPEG files and converting them to RGB |
| `matplotlib` | Displaying images and the zoom/rotate results |
| `flake8` | The 42 code norm (`norminette`) |
| `black` | Code formatting (`make format`) |
