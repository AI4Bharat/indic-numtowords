"""Regression tests. Run with: python -m pytest tests"""

import re
import unicodedata

import pytest

from indic_numtowords import num2words as _num2words


def num2words(*args, **kwargs):
    # The data files mix composed and decomposed vowel signs (e.g. Kannada "ೊ"
    # as U+0CCA or U+0CC6 U+0CC2); they render the same, so compare as NFC.
    return unicodedata.normalize("NFC", _num2words(*args, **kwargs))


@pytest.mark.parametrize(
    "number, expected",
    [
        (110, "ನೂರಹತ್ತು"),
        (150, "ನೂರೈವತ್ತು"),
        (510, "ಐನೂರಹತ್ತು"),
        (290, "ಇನ್ನೂರತೊಂಬತ್ತು"),
        (1150, "ಒಂದು ಸಾವಿರದ ನೂರೈವತ್ತು"),
    ],
)
def test_kannada_exact_tens_after_hundreds(number, expected):
    assert num2words(number, lang="kn") == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1000, "ಒಂದು ಸಾವಿರ"),
        (24000, "ಇಪ್ಪತ್ನಾಲ್ಕು ಸಾವಿರ"),
        (200000, "ಎರಡು ಲಕ್ಷ"),
        (10500000, "ಒಂದು ಕೋಟಿ ಐದು ಲಕ್ಷ"),
        (1001, "ಒಂದು ಸಾವಿರದ ಒಂದು"),  # joining form still used before a number
    ],
)
def test_kannada_round_thousands_and_lakhs(number, expected):
    assert num2words(number, lang="kn") == expected


def test_kannada_83_is_not_82():
    assert num2words(83, lang="kn") == "ಎಂಬತ್ಮೂರು"
    assert num2words(83, lang="kn") != num2words(82, lang="kn")


def test_kannada_two_digit_numbers_are_unique():
    words = [num2words(n, lang="kn") for n in range(100)]
    assert len(set(words)) == 100


@pytest.mark.parametrize(
    "lang",
    ["as", "bn", "en", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te", "ur"],
)
def test_no_stray_or_zero_width_whitespace(lang):
    for n in range(0, 100000, 7):
        words = num2words(n, lang=lang)
        assert words == words.strip() and "  " not in words, (n, words)
        assert not re.search(r"[\u200b\u200c]", words), (n, words)


def test_split_and_long_numbers_accept_int():
    assert num2words(420, lang="hi", split=True) == "चार दो शून्य"
    assert num2words(420, lang="doi", split=True) == "चार दो सिफर"  # README example
    assert num2words(9987761000, lang="hi") == num2words("9987761000", lang="hi")
