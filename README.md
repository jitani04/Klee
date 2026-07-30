# Symbolic Execution of libtiff with KLEE

Symbolic-execution artifacts and analysis tooling produced by running the
[KLEE](https://klee-se.org/) engine on **libtiff's `tiffcp`** utility to
automatically generate high-coverage test inputs and surface potential bugs.

## What's here

- **KLEE run output** — generated test cases (`test*.ktest`), coverage/run
  statistics (`run.stats`, `run.istats`), and logs (`messages.txt`, `warnings.txt`).
- **`klee_parser.py`** — a short script that loads `.ktest` files with KLEE's
  `KTest` API to inspect the concrete inputs KLEE synthesized for each path.
- **`assembly.ll`** — the LLVM IR the analysis was run against.

## How it was run

```
klee --libc=uclibc --posix-runtime --max-time=300 --max-memory=2048 \
     --max-sym-array-size=512 --only-output-states-covering-new \
     tiffcp_for_klee_magic.bc
```

KLEE explores program paths symbolically and emits a concrete test case
(`.ktest`) for each path it covers, including error cases
(e.g. `test000007.external.err`). These inputs can be replayed against the
native binary to reproduce crashes or measure coverage.

## Reading a test case

```bash
python klee_parser.py     # prints the symbolic object data from a .ktest file
```

## Topics

Symbolic execution, automated test generation, coverage-guided analysis,
software security, LLVM.
