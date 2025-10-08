import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import currency_converter


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        """Set a constant conversion rate for all tests in this class."""
        self.conversion_rate = 83.50

    def test_usd_to_inr(self):
        """Tests standard conversions."""
        # Use assertAlmostEqual for floating-point comparisons
        self.assertAlmostEqual(currency_converter.usd_to_inr(1, self.conversion_rate), 83.50)
        self.assertAlmostEqual(currency_converter.usd_to_inr(10, self.conversion_rate), 835.0)
        self.assertAlmostEqual(currency_converter.usd_to_inr(0, self.conversion_rate), 0)
        self.assertAlmostEqual(currency_converter.usd_to_inr(0.5, self.conversion_rate), 41.75)

    def test_invalid_input(self):
        """Tests that the function raises appropriate ValueErrors."""
        with self.assertRaises(ValueError):
            currency_converter.usd_to_inr(-50)
            
        with self.assertRaises(ValueError):
            currency_converter.usd_to_inr("fifty")


if __name__ == '__main__':
    unittest.main()