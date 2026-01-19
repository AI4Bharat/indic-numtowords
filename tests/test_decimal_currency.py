"""
Tests for decimal and currency conversion functionality.

Tests the new features added in v1.1.0:
- Decimal number conversion (e.g., 42.5 -> "forty-two point five")
- Currency formatting (e.g., 42.50 INR -> "forty-two rupees and fifty paise")
"""

import pytest
from indic_numtowords import num2words, decimal_point_words, currency_formats


class TestDecimalConversion:
    """Tests for decimal/float number conversion."""

    def test_simple_decimal_english(self):
        """Test basic decimal conversion in English."""
        result = num2words(42.5, lang="en")
        assert result == "forty-two point five"

    def test_decimal_with_multiple_digits(self):
        """Test decimal with multiple fractional digits."""
        result = num2words(3.14, lang="en")
        assert result == "three point one four"

    def test_decimal_with_leading_zero_fraction(self):
        """Test decimal like 5.05."""
        result = num2words(5.05, lang="en")
        assert result == "five point zero five"

    def test_decimal_string_input(self):
        """Test decimal passed as string."""
        result = num2words("123.456", lang="en")
        assert result == "one hundred and twenty-three point four five six"

    def test_decimal_hindi(self):
        """Test decimal conversion in Hindi."""
        result = num2words(42.5, lang="hi")
        assert "दशमलव" in result  # Contains decimal point word

    def test_decimal_tamil(self):
        """Test decimal conversion in Tamil."""
        result = num2words(10.5, lang="ta")
        assert "புள்ளி" in result  # Contains decimal point word

    def test_whole_number_as_float(self):
        """Test whole number passed as float (e.g., 100.0)."""
        result = num2words(100.0, lang="en")
        assert result == "one hundred point zero"

    def test_zero_decimal(self):
        """Test zero with decimal."""
        result = num2words(0.5, lang="en")
        assert result == "zero point five"


class TestCurrencyConversion:
    """Tests for currency formatting."""

    def test_inr_simple_english(self):
        """Test simple INR conversion in English."""
        result = num2words(42.50, lang="en", currency="INR")
        assert result == "forty-two rupees and fifty paise"

    def test_inr_no_paise(self):
        """Test INR with no paise (whole rupees)."""
        result = num2words(100, lang="en", currency="INR")
        assert result == "one hundred rupees"
        assert "paise" not in result

    def test_inr_single_paise(self):
        """Test INR with single digit paise."""
        result = num2words(50.05, lang="en", currency="INR")
        assert result == "fifty rupees and five paise"

    def test_inr_hindi(self):
        """Test INR in Hindi."""
        result = num2words(100.25, lang="hi", currency="INR")
        assert "रुपये" in result
        assert "पैसे" in result
        assert "और" in result

    def test_inr_tamil(self):
        """Test INR in Tamil."""
        result = num2words(50.75, lang="ta", currency="INR")
        assert "ரூபாய்" in result
        assert "பைசா" in result

    def test_inr_bengali(self):
        """Test INR in Bengali."""
        result = num2words(25.50, lang="bn", currency="INR")
        assert "টাকা" in result
        assert "পয়সা" in result

    def test_inr_large_amount(self):
        """Test INR with large amount."""
        result = num2words(1234.56, lang="en", currency="INR")
        assert "one thousand two hundred and thirty-four rupees" in result
        assert "fifty-six paise" in result

    def test_inr_string_input(self):
        """Test currency with string input."""
        result = num2words("99.99", lang="en", currency="INR")
        assert result == "ninety-nine rupees and ninety-nine paise"

    def test_integer_with_currency(self):
        """Test integer with currency flag."""
        result = num2words(500, lang="en", currency="INR")
        assert result == "five hundred rupees"

    def test_unsupported_currency(self):
        """Test that unsupported currency raises error."""
        with pytest.raises(ValueError, match="Currency .* is not supported"):
            num2words(100, lang="en", currency="USD")


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_invalid_string_input(self):
        """Test that invalid string raises error."""
        with pytest.raises(ValueError):
            num2words("not a number", lang="en")

    def test_unsupported_language(self):
        """Test that unsupported language raises error."""
        with pytest.raises(ValueError, match="Language not supported"):
            num2words(42, lang="xx")

    def test_decimal_with_commas(self):
        """Test decimal string with comma separators."""
        result = num2words("1,234.56", lang="en")
        assert "one thousand two hundred and thirty-four" in result

    def test_negative_decimal(self):
        """Test negative decimal number."""
        result = num2words(-42.5, lang="en")
        assert "minus" in result
        assert "forty-two point five" in result

    def test_negative_currency(self):
        """Test negative currency amount."""
        result = num2words(-100.50, lang="en", currency="INR")
        assert "minus" in result


class TestBackwardsCompatibility:
    """Tests to ensure existing functionality still works."""

    def test_integer_conversion(self):
        """Test that integer conversion still works."""
        result = num2words(42, lang="en")
        assert result == "forty-two"

    def test_variations_still_work(self):
        """Test that variations parameter still works."""
        result = num2words(150, lang="hi", variations=True)
        assert isinstance(result, list)

    def test_split_still_works(self):
        """Test that split parameter still works."""
        result = num2words(123, lang="en", split=True)
        assert "one" in result
        assert "two" in result
        assert "three" in result

    def test_string_integer_input(self):
        """Test string integer input."""
        result = num2words("42", lang="en")
        assert result == "forty-two"


class TestAllLanguagesDecimalSupport:
    """Test decimal point words exist for all supported languages."""

    def test_all_supported_langs_have_decimal_words(self):
        """Verify all languages have decimal point words."""
        from indic_numtowords.numtowords import supported_langs, extended_supported_langs

        all_langs = supported_langs + extended_supported_langs
        for lang in all_langs:
            assert lang in decimal_point_words, f"Missing decimal word for {lang}"

    def test_all_supported_langs_have_inr_currency(self):
        """Verify all languages have INR currency support."""
        from indic_numtowords.numtowords import supported_langs, extended_supported_langs

        all_langs = supported_langs + extended_supported_langs
        for lang in all_langs:
            assert lang in currency_formats["INR"], f"Missing INR currency for {lang}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
