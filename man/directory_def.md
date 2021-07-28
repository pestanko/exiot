# Directory tests definition

This is the simplest test definition, where you are defining the tests by creating files with special extensions
[(explained bellow)](#Test Definition).

Directory structure definition supports:

- **single suite** - all tests in the root directory
- **multi suite** - tests root dir contains another directories _(suites)_ that contains tests.

## Test Definition

Tests are defined by files with the same file name (without extension). Example: ``simple_test.out``, `simple_test.in`,
defines the single test ``simple_test``

### File Extensions

Supported file extensions:

- ``.args`` - defines the provided executable arguments - single argument on the new line
- ``.in`` - defines the provided `stdin` for the executable
- ``.out`` - defines the expected `stdout` for the executable
- ``.err`` - defines the expected `stderr` for the executable+
- ``.exit`` - defines the expected _exit code_ (_return code_) for the executable
- ``.env``  - defines the environment variables
- ``.files`` - defines the files mapping, where you define provided and expected file content validation

Exit file format `<INT_NUMBER|any|non-zero>`.

Env file format `NAME=VALUE`:

```shell
ENV_VAR=env value
ENV_VAR2=env value2
```

Files format `<EXPECTED><SEMICOLON><PROVIDED><NEW_LINE>`:

```
EXPECTED;PROVIDED

# EXAMPLES:
data/expected_generated.txt;my_generated_file.txt
data/expected_super.txt;my_super_file.txt
```

## Single Suite Structure

All the tests are defined in single root directory

Example:

```
tests_root/
    - test1.in
    - test1.out
    - test2.args
    - test2.err
    - test2.out
    - failing_test.in
    - failing_test.err
```

This example contains 3 tests: ``test1``, `test2`, `failing_test`


## Multi Suite Structure

Tests are defined in subdirectories, where each sub-directory is separete test-suite (tests collection).

Example:

```
tests_root/
    - suite1/
        - test1.in
        - test1.out
    - suite2/
        - hello_world.out
        - cat_test.in
        - cat_test.out
    - suite3/
        - echo_hello.args
        - echo_hello.out
        - echo_hello_world.out
        - echo_hello_world.args
```

Tests root directory contains 3 suites, where first suite contains just one test, second contains 2 tests and third contains also two tests.

