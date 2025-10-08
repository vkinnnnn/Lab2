import pytest
from src import currency_converter

# A constant conversion rate for consistent testing
TEST_RATE = 83.50

def test_usd_to_inr():
    """Tests the usd_to_inr conversion function."""
    assert currency_converter.usd_to_inr(1, TEST_RATE) == 83.50
    assert currency_converter.usd_to_inr(10, TEST_RATE) == 835.0
    assert currency_converter.usd_to_inr(0, TEST_RATE) == 0
    # Test with floating point values
    assert currency_converter.usd_to_inr(0.5, TEST_RATE) == 41.75

def test_invalid_input():
    """Tests that the function raises errors for invalid input."""
    with pytest.raises(ValueError):
        currency_converter.usd_to_inr(-10)  # Negative amount
    
    with pytest.raises(ValueError):
        currency_converter.usd_to_inr("one hundred")  # Non-numeric string