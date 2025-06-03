# Python Programming Assessment

This assessment consists of several Python programming challenges designed to test your skills in:

1.  String Manipulation (`StringProcessor`)
2.  Number Processing (`NumberCruncher`)
3.  Logical Operations (`LogicValidator`)
4.  Test-Driven Development (TDD) (`PasswordValidatorTDD`)

## Files

*   **`assessment.py`**: This file contains the Python classes and method skeletons you need to implement. Each method has a docstring explaining its requirements. **Do not change the method signatures.**
*   **`test_assessment.py`**: This file contains unit tests to help you verify your solutions.
    *   Tests for `StringProcessor`, `NumberCruncher`, and `LogicValidator` are already complete. You can run them to check your implementations for these sections.
    *   For `PasswordValidatorTDD`, you **must first write the tests** in the `TestPasswordValidatorTDD` class within `test_assessment.py` *before* you implement the `is_valid_password` method in `assessment.py`. This is the Test-Driven Development part of the assessment.
    *   There is an additional test suite, `TestStudentPasswordTestsEffectiveness`, which is designed to check if the tests you write for `PasswordValidatorTDD` are effective at catching common errors. If your TDD tests are well-written, this meta-test suite should pass.

## Instructions

1.  **Implement Solutions**: Fill in the methods in `assessment.py` according to the docstring specifications.
2.  **Test-Driven Development for `PasswordValidatorTDD`**:
    *   Open `test_assessment.py`.
    *   Locate the `TestPasswordValidatorTDD` class.
    *   Write comprehensive test cases for the `is_valid_password` method based on its requirements (detailed in `assessment.py`). Think about valid passwords, and various invalid passwords that miss one or more criteria (e.g., too short, no uppercase, no digit, no special character, etc.).
    *   Initially, these tests should fail because you haven't implemented `is_valid_password` yet.
    *   Then, implement the `is_valid_password` method in `assessment.py` until all the tests you wrote in `TestPasswordValidatorTDD` pass.
3.  **Run Tests**:
    You can run the tests from your terminal in the directory containing these files:
    ```bash
    python -m unittest test_assessment.py
    ```
    Or, if you want more verbose output:
    ```bash
    python -m unittest -v test_assessment.py
    ```
    Your goal is to make all tests pass, including `TestStudentPasswordTestsEffectiveness` (which relies on your `TestPasswordValidatorTDD` tests being effective).

## Important Notes

*   Do not modify the method signatures (name, parameters, type hints) in `assessment.py`.
*   Do not modify the existing completed tests in `test_assessment.py` (except for uncommenting and filling in `TestPasswordValidatorTDD`).
*   The `TestStudentPasswordTestsEffectiveness` suite will attempt to run your `TestPasswordValidatorTDD` tests against deliberately flawed versions of `is_valid_password`. If your tests don't catch these flaws, the meta-test will fail, indicating your TDD tests need improvement.

Good luck!