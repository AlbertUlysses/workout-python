""" Tests for chapter 2.
"""
from chapter2 import pig_latin, pl_sentence, ubbi_dubbi, strsort


def test_vowel_pig_latin():
    """Tests the pig_latin function with a word that starts with a vowel."""
    eat_expected = "eatway"
    eat_result = pig_latin("eat")
    assert eat_expected == eat_result


def test_consonant_pig_latin():
    """Tests the pig_latin function with a word that starts with a consonant."""
    python_expected = "ythonpay"
    python_result = pig_latin("python")
    assert python_expected == python_result


def test_pl_sentence():
    """Tests pl_sentence function."""
    expected = "histay isway away esttay ranslationtay"
    result = pl_sentence("this is a test translation")
    assert expected == result


def test_ubbi_dubbi():
    """Test ubbi_dubbi function."""
    expected = "uboctubopubus"
    result = ubbi_dubbi("octopus")
    assert expected == result


def test_strsort():
    """Test strsort"""
    expected = "abc"
    result = strsort("cba")
    assert expected == result
