# Module 4 — Data-oriented design

## Overview

Module 4 places state deliberately. The subject moves from keyword dispatch,
through closures and decorator factories, to dataclasses, and every exercise asks
the same question in a different form: who owns this value, and when does it
change? Detailed explanations and reproducible transcripts are kept in
[`Docs/`](Docs/).

## Objectives

By the end of the module, we can dispatch work through the values of `**kwargs`,
compute order statistics without a library, keep state alive in a closure cell,
rebuild a decorator factory from its three scopes, and declare derived state with
`field(init=False)` and `__post_init__`. We also learn that the subject requires a
docstring on every function and class, and that flake8 does not check that rule.

## Exercises

| Exercise | Subject | Documentation |
| --- | --- | --- |
| Exercice 00 | Calculate statistics | [Read the exercise doc](Docs/ex00.md) |
| Exercice 01 | Outer_inner | [Read the exercise doc](Docs/ex01.md) |
| Exercice 02 | My first decorating | [Read the exercise doc](Docs/ex02.md) |
| Exercice 03 | Data class | [Read the exercise doc](Docs/ex03.md) |
