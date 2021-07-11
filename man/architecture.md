# Architecture

Simple description of the internal architecture.

Project -> Suite -> Test

At the top level there is **Project**, project can consits from multiple **Suites**, each suite can contain multiple **Tests**.

Each Project, Suite and Test (let's call them entities) has these common fields:
- _metadata_ contains information about the entity like (it's _name_, _description_, ...)
- _settings_ contains configuration that is passed down to the runtime that would evaluate _tests_

Project and Suite are mostly namespaces that are grouping tests and it's results - but tests are the most important part.

## Test

Test consists of:
- _preconditions_: whether test should be executed or not
- _action_: what action should be executed (default: 'exec', execute the command)
- _validators_: List of validation checks that will test whether the _action_ was executed properly






