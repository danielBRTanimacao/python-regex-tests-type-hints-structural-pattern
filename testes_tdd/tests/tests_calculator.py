import unittest
from calculator import sum_, mult_

class TestCalculator(unittest.TestCase):
    def test_sum_number_with_number_to_return_number(self):
        self.assertEqual(sum_(1, 1), 2)

    def test_multiply_number_with_other_number_return_number(self):
        self.assertEqual(mult_(2, 2), 4)

    def test_multiply_number_with_other_number_return_number_with_diversaus_returns(self):
        x_y_returns = (
            (10, 10, 100),
            (1, 10, 10),
            (2, 8, 16),
            (2, 4, 8),
        )

        for scape in x_y_returns:
            with self.subTest(x_y_returns=x_y_returns):
                x, y, scape_ = scape
                self.assertEqual(mult_(x, y), scape_)

    def test_if_is_assertion_error_in_variables(self):
        with self.assertRaises(AssertionError):
            sum_('10', 10)


unittest.main(verbosity=2)