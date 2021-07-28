# Scenario definition

Scenario definition is the "best way" to define you tests - it provides most flexibility.

Scenarios can be defined using ``json`` or `yml` (for _yml_ you need `PyYaml` library installed).

## Project Definition

It has to be defined in the `project.yml` or `project.json` file.

```yaml
project:
    name: sample_project
    desc: Sample project definition

params:
    valgrind: true
    timeout: 100

suites:
    - "suite*.yml" # YES you can use globs, because why not!
    - "my_super_suite.yml"
```

## Suite Definition

It is best to define suites in ``suite_*.{yml|json}`` files.

```yaml
suite:
    name: sample_suite
    desc: Sample suite definition

params:
    valgrind: false

tests:
    - name: cat single hello
      desc: "cat out the hello"
      args: [ 'cat' ]
      in: data/single_hello.out
      out: data/single_hello.out
      exit: 0

    - name: cat hello world
      desc: "cat out the hello world"
      args: [ 'cat', 'single_hello.out' ]
      data:
          - data/single_hello.out
      out: data/single_hello.out

    - name: cat hello world stderr
      desc: "cat out the hello world to stderr"
      args: [ 'cat', 'single_hello.out', 'stderr' ]
      data:
          - data/single_hello.out
      env:
          LD_PRELOAD: "/opt/lib_override.so"
          NICE_TEST: "test"
      err: data/single_hello.out

    - name: cat hello world to file
      desc: "cat out the hello world"
      args: [ 'cat', 'single_hello.out', 'hello.txt' ]
      data:
          - data/single_hello.out
      out:
          empty: true
      files:
          - provided: 'hello.txt'
            expected: 'data/single_hello.out'
```

## Test definition

Test definition is a part of the ``suite`` definition take a look above - the `tests:` property.

### Supported properties

Supported properties for the test:

- `name` - name of the test
- `desc` - Test description (Optional)
- `args` - List of executable arguments
- `exit` - Exit code assertion (`<INT_VAL|any|non-zero>`)
- `env` - Environment variables for the executable
- `data` - which files to copy from the tests root directory to the workspace
- `in` - STDIN definition for the executable, see [here](#STDIN Definition)
- `err` - STDERR definition assertion for the executable, see [here](#File Assertion Definition)
- `out` - STDOUT definition assertion for the executable, see [here](#File Assertion Definition)
- `files` - List of file assertions

#### Exit code assertion Definition

It can be multiple values:

- `non-zero` - will check whether exit is non-zero
- `<NUMBER>` - will be parsed to ``int``
- `any` - any value - it will not be checked

#### STDIN Definition

Can be either string or dictionary/map.

If the value is string, it can be either:
- `empty` - no input
- any other value will be interpreted as file path to the file

If the value is `dictionary`, it can contain properties:
- ``file`` - file location
- ``content`` - string content of the file

#### File Assertion Definition

Can be either string or dictionary/map.

If the value is string, it can be either:
- `any` - it will not be checked
- `empty` - the file size should be zero
- `non-empty|nonempty` - file size should be greater than zero
- any other value will be interpreted as file path to the file

If the value is dictionary, it can contain properties:
- `any` - do not check
- `empty` - if `true` it should be empty - file size 0, if `false` it should be non-empty
- `size` - expect the exact size
- `match` - defines the `regex`, that the file output should match
- `content` - defines the expected text content against which the file will be asserted
- `file|path` - asserts the output content would match the file
- `base64` - base64 encoded content (otherwise same as `content`)


