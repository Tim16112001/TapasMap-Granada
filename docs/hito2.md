# Hito 2 – Continuous Integration (CI)

## Task Runner
For this project, I used **pytest** as the test framework and **GitHub Actions** for CI.
`pytest` was chosen because it is simple, powerful, and widely used for Python projects.

## Assertion Library
The built-in `assert` statements are used for simplicity.

## Test Runner
`pytest` automatically discovers and runs all tests that start with `test_`.

## CI System
GitHub Actions was configured to automatically run the tests whenever code is pushed or a pull request is made. This ensures code quality and avoids integration errors.

## Example Test
```python
def test_sum():
    result = 2 + 3
    assert result == 5
