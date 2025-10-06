# Hito 2 – Continuous Integration (CI)

## 1. Milestone Goal

- Implement Continuous Integration (CI) for the TapasMap project
- Add automated tests to ensure code quality
- Set up virtual environment and project dependencies
- Document all Hito 2 steps

---

## 2. Virtual Environment & Dependencies

1. **Created virtual environment**
   python -m venv venv
   venv\Scripts\activate  # Windows
2. **Installed project dependencies**
   pip install -r requirements.txt
   pip install pytest
3. **Test Framework Setup**
   1. Task Runner
      - Used pytest as the test framework
      - Chosen because it is simple, widely used, and powerful for Python projects
    2. Assertion Library
       - Used Python built-in assert statements for simplicity
    3. Test Runner
       - pytest automatically discovers and runs all test functions starting with test_
    4. Example Test
       - def test_add_bar():
            from tapas import add_bar, tapas_bars
            tapas_bars.clear()
            result = add_bar("Bar Example", "Granada")
            assert result is True
             assert tapas_bars[0]["name"] == "Bar Example"
            assert tapas_bars[0]["city"] == "Granada"


