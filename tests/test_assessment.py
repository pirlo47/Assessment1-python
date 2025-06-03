import unittest
from unittest.mock import patch
import io
import sys
from assessment import StringProcessor, NumberCruncher, LogicValidator, PasswordValidatorTDD

class TestStringProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = StringProcessor()

    def test_reverse_words_basic_sentence(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("Hello World"), "olleH dlroW")

    def test_reverse_words_with_punctuation(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("Python is fun!"), "nohtyP si !nuf")

    def test_reverse_words_single_word(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("Test"), "tseT")

    def test_reverse_words_empty_string(self):
        self.assertEqual(self.processor.reverse_words_in_sentence(""), "")

    def test_reverse_words_multiple_spaces_preserved(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("Word1  Word2"), "1droW  2droW")

    def test_reverse_words_leading_trailing_spaces_preserved(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("  leading"), "  gnidael")
        self.assertEqual(self.processor.reverse_words_in_sentence("trailing  "), "gniliart  ")
        self.assertEqual(self.processor.reverse_words_in_sentence("  both  "), "  htob  ")

    def test_reverse_words_string_with_only_spaces(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("   "), "   ")

    def test_reverse_words_single_letters(self):
        self.assertEqual(self.processor.reverse_words_in_sentence("a b c"), "a b c")

class TestNumberCruncher(unittest.TestCase):
    def setUp(self):
        self.cruncher = NumberCruncher()

    def test_process_numbers_mixed_positive(self):
        numbers = [1, 2, 3, 4, 5]
        expected = {"sum_of_evens": 6, "product_of_odds": 15}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_only_evens_with_zero(self):
        numbers = [2, 4, 6, 0]
        expected = {"sum_of_evens": 12, "product_of_odds": 1}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_only_odds(self):
        numbers = [1, 3, 5, 7]
        expected = {"sum_of_evens": 0, "product_of_odds": 105}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_empty_list(self):
        numbers = []
        expected = {"sum_of_evens": 0, "product_of_odds": 1}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_with_negatives(self):
        numbers = [-1, -2, -3, -4, 5, 0]
        expected = {"sum_of_evens": -6, "product_of_odds": 15} #
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_all_zeros(self):
        numbers = [0, 0, 0]
        expected = {"sum_of_evens": 0, "product_of_odds": 1}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_no_odds(self):
        numbers = [2, 4, 8]
        expected = {"sum_of_evens": 14, "product_of_odds": 1}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)

    def test_process_numbers_no_evens(self):
        numbers = [1, 3, 7]
        expected = {"sum_of_evens": 0, "product_of_odds": 21}
        self.assertEqual(self.cruncher.process_numbers(numbers), expected)


class TestLogicValidator(unittest.TestCase):
    def setUp(self):
        self.validator = LogicValidator()

    def test_senior_discount_various_conditions(self):
        self.assertEqual(self.validator.check_discount_eligibility(65, False, False), "Senior Discount")
        self.assertEqual(self.validator.check_discount_eligibility(70, True, True), "Senior Discount")
        self.assertEqual(self.validator.check_discount_eligibility(100, True, False), "Senior Discount")

    def test_student_discount_various_conditions(self):
        self.assertEqual(self.validator.check_discount_eligibility(17, False, False), "Student Discount")
        self.assertEqual(self.validator.check_discount_eligibility(10, True, True), "Student Discount")
        self.assertEqual(self.validator.check_discount_eligibility(0, False, True), "Student Discount")

    def test_member_coupon_discount_adult(self):
        self.assertEqual(self.validator.check_discount_eligibility(30, True, True), "Member Coupon Discount")
        self.assertEqual(self.validator.check_discount_eligibility(18, True, True), "Member Coupon Discount")
        self.assertEqual(self.validator.check_discount_eligibility(64, True, True), "Member Coupon Discount")

    def test_member_discount_adult(self):
        self.assertEqual(self.validator.check_discount_eligibility(30, True, False), "Member Discount")
        self.assertEqual(self.validator.check_discount_eligibility(18, True, False), "Member Discount")
        self.assertEqual(self.validator.check_discount_eligibility(64, True, False), "Member Discount")

    def test_coupon_discount_adult(self):
        self.assertEqual(self.validator.check_discount_eligibility(30, False, True), "Coupon Discount")
        self.assertEqual(self.validator.check_discount_eligibility(18, False, True), "Coupon Discount")
        self.assertEqual(self.validator.check_discount_eligibility(64, False, True), "Coupon Discount")

    def test_no_discount_adult(self):
        self.assertEqual(self.validator.check_discount_eligibility(30, False, False), "No Discount")
        self.assertEqual(self.validator.check_discount_eligibility(18, False, False), "No Discount")
        self.assertEqual(self.validator.check_discount_eligibility(64, False, False), "No Discount")

# -----------------------------------------------------------------------------
# STUDENT TDD SECTION: Implement tests in TestPasswordValidatorTDD first!
# -----------------------------------------------------------------------------
class TestPasswordValidatorTDD(unittest.TestCase):
    # NOTE TO STUDENT: Implement these tests *before* implementing the
    # PasswordValidatorTDD.is_valid_password method in assessment.py.
    # Think about edge cases and all conditions mentioned in the docstring.

    def setUp(self):
        # This instance will be used by your test methods.
        # The meta-tests below will patch PasswordValidatorTDD directly from the assessment module.
        self.validator = PasswordValidatorTDD()

    # TODO: STUDENT - Write your test methods here. Examples:
    #
    # def test_valid_password_meets_all_criteria(self):
    #     """Test a password that meets all criteria."""
    #     # self.assertTrue(self.validator.is_valid_password("ValidPass1!"))
    #     pass
    #
    # def test_invalid_too_short(self):
    #     """Test password shorter than 8 characters."""
    #     # self.assertFalse(self.validator.is_valid_password("Sh0rt!"))
    #     pass
    #
    # def test_valid_minimum_length(self):
    #     """Test password at the minimum length (8 characters) meeting all other criteria."""
    #     # self.assertTrue(self.validator.is_valid_password("MinLenA1@"))
    #     pass
    # Add at least 5-7 more diverse test cases covering all rules and edge cases.
    # Ensure your tests in this class collectively cover all conditions described in
    # the PasswordValidatorTDD.is_valid_password docstring.
    pass # REMOVE THIS PASS AND ADD YOUR TESTS

# -----------------------------------------------------------------------------
# META-TESTS: To check the effectiveness of student's TDD tests for PasswordValidatorTDD
# Students should NOT modify this class.
# -----------------------------------------------------------------------------

# --- Flawed Implementations for Meta-Testing ---
def flawed_is_valid_always_true(self, password: str) -> bool:
    return True

def flawed_is_valid_length_only(self, password: str) -> bool:
    # Only checks length, misses other criteria
    return 8 <= len(password) <= 30

def flawed_is_valid_no_uppercase_check(self, password: str) -> bool:

    if not (8 <= len(password) <= 30): return False

    if not any('a' <= char <= 'z' for char in password): return False
    if not any('0' <= char <= '9' for char in password): return False
    if not any(char in "!@#$%^&*()-_+=" for char in password): return False
    return True

def flawed_is_valid_no_special_check(self, password: str) -> bool:

    if not (8 <= len(password) <= 30): return False
    if not any('A' <= char <= 'Z' for char in password): return False
    if not any('a' <= char <= 'z' for char in password): return False
    if not any('0' <= char <= '9' for char in password): return False

    return True

class TestStudentPasswordTestsEffectiveness(unittest.TestCase):
    """
    This test suite checks if the student's tests in TestPasswordValidatorTDD
    are effective at catching common flaws in a password validation logic.
    It does this by running the student's tests against known-bad implementations.
    If a student's test suite passes against a bad implementation, it means
    their tests are not comprehensive enough to catch that specific flaw.
    """

    def _run_student_tests_with_patched_validator(self, flawed_method):
        """
        Helper to run student's TestPasswordValidatorTDD suite with a patched
        is_valid_password method.
        Returns True if the student's test suite FAILED (i.e., caught the flaw),
        False otherwise.
        """

        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

        try:

            with patch('assessment.PasswordValidatorTDD.is_valid_password', new=flawed_method):
                # Important: We need to reload tests from TestPasswordValidatorTDD *after* the patch
                # is in place, because its setUp method creates a PasswordValidatorTDD instance.
                # Or, ensure the patch affects the instance created in setUp.
                # The patch on 'assessment.PasswordValidatorTDD.is_valid_password' should affect
                # any new instance of PasswordValidatorTDD from that module.

                suite = unittest.TestLoader().loadTestsFromTestCase(TestPasswordValidatorTDD)
                if suite.countTestCases() == 0:
                    # If no tests are found, we can't determine if the flaw is caught.
                    print("\nWarning: No tests found in TestPasswordValidatorTDD. Student needs to write them.", file=original_stderr)
                    return False

                result = unittest.TextTestRunner(stream=sys.stdout, verbosity=0).run(suite)

                return not result.wasSuccessful()
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr

    def test_student_tests_catch_always_true_flaw(self):
        """
        Student's tests should fail if is_valid_password always returns True.
        """
        caught_flaw = self._run_student_tests_with_patched_validator(flawed_is_valid_always_true)
        self.assertTrue(caught_flaw,
                        "Student's TDD tests for PasswordValidatorTDD did not "
                        "catch a flaw where is_valid_password always returns True. "
                        "Ensure tests include passwords that should be invalid.")

    def test_student_tests_catch_length_only_flaw(self):
        """
        Student's tests should fail if is_valid_password only checks length.
        """
        caught_flaw = self._run_student_tests_with_patched_validator(flawed_is_valid_length_only)
        self.assertTrue(caught_flaw,
                        "Student's TDD tests for PasswordValidatorTDD did not "
                        "catch a flaw where is_valid_password only checks length "
                        "(missing upper/lower/digit/special char checks). "
                        "Ensure tests cover these specific missing criteria.")

    def test_student_tests_catch_no_uppercase_check_flaw(self):
        """
        Student's tests should fail if is_valid_password doesn't check for uppercase.
        """
        caught_flaw = self._run_student_tests_with_patched_validator(flawed_is_valid_no_uppercase_check)
        self.assertTrue(caught_flaw,
                        "Student's TDD tests for PasswordValidatorTDD did not "
                        "catch a flaw where the uppercase letter check is missing. "
                        "Ensure tests include passwords valid in all ways except missing an uppercase letter.")

    def test_student_tests_catch_no_special_char_check_flaw(self):
        """
        Student's tests should fail if is_valid_password doesn't check for special chars.
        """
        caught_flaw = self._run_student_tests_with_patched_validator(flawed_is_valid_no_special_check)
        self.assertTrue(caught_flaw,
                        "Student's TDD tests for PasswordValidatorTDD did not "
                        "catch a flaw where the special character check is missing. "
                        "Ensure tests include passwords valid in all ways except missing a special character.")


if __name__ == '__main__':
    # Ensure that when running this file directly, the 'assessment' module can be found.
    # This typically means 'assessment.py' is in the same directory or Python's path.
    unittest.main(verbosity=2)