# Architecture

Simple description of the internal architecture.

Project -> Suite -> Test (three structure where the Project is the root)

At the top level there is **Project**, project can consist from multiple **Suites**,
each suite can contain multiple **Tests**.

Each Project, Suite and Test (let's call them entities) has these common fields:
- `id` - Unique identifier - from sanitized name
- `name` - Name
- `desc` - Description
- `namespace` - fully-qualified namespace (string representation for test: `/project_id/suite_id/test_id`)
- `params` - Optional parameters - that are propagated from Project -> Suite -> Test

Project and Suite are mostly namespaces that are groups of tests and it's results - but tests are the most important part.
Project and Suite params are shared among all the tests.

## Test

Test consists of:

- _preconditions_: whether test should be executed or not
- _action_: what action should be executed (default: 'exec', execute the command)
- _validations_: List of validation checks that will test whether the _action_ was executed properly






