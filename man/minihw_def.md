# MiniHw Directory tests definition

Parser: ``minihw``

This is extension of the [Directory Definition](./directory_def.md) so take a look at there.

MiniHw is multi-suite definition directory type, it means that the root directory contains other directories, where each
directory is different suite.

## Difference between the MiniHw tests and Directory definition

Each MihiHw suite contains 3 additional files (`source.c`, `solution.c`, `CMakeLists.txt`), where:

- `source.c` contains the prepared source (to be implemented) with assignment.
- `solution.c` contains the solution, reference implementation of the assignment
- `CMakeLists.txt` build instructions for `cmake`

In order to test ``source.c`` you can just execute:

```bash
python -m exiot exec -p minihw <TESTS_PATH>
# OR define target explicitelly
python -m exiot exec -p minihw -D 'target=source' <TESTS_PATH>
# Example:
python -m exiot exec -p minihw -D 'target=source' examples/minihw_not_impl
```

In order to test ``solution.c`` you can just execute:

```bash
python -m exiot exec -p minihw -D 'target=solution' <TESTS_PATH>
# Example:
python -m exiot exec -p minihw -D 'target=solution' examples/minihw_not_impl
```

