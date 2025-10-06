# Hito 2 – Continuous Integration (CI)

1. Milestone Goal
Implement Continuous Integration for the TapasMap project
Add automated tests to ensure code quality
Set up virtual environment and dependencies
Document all Hito 2 steps

2. Virtual Environment Setup
Created virtual environment using `python -m venv venv`
Activated virtual environment
Installed project dependencies listed in `requirements.txt`
Installed `pytest` as the test framework

3. Test Framework Setup
Task Runner: `pytest` chosen for simplicity and wide usage in Python
Assertion Library: Python's built-in `assert` statements used for checks
Test Runner: `pytest` automatically discovers and runs all test functions starting with `test_`
Example Test:
```python
def test_add_bar():
    from tapas import add_bar, tapas_bars
    tapas_bars.clear()
    result = add_bar("Bar Example", "Granada")
    assert result is True
    assert tapas_bars[0]["name"] == "Bar Example"
    assert tapas_bars[0]["city"] == "Granada"

