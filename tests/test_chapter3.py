""" Tests for chapter 3.
"""
from chapter3 import (
    firstlast,
    mysum,
    alphabetize_name,
    most_repeating_word,
    format_sort_records,
)


def test_firstlast_strings():
    """Test for firstlast function with strings."""
    expected = "ac"
    result = firstlast("abc")
    assert expected == result


def test_firstlast_list():
    """Test for firstlast function with lists."""
    expected = [1, 4]
    result = firstlast([1, 2, 3, 4])
    assert expected == result


def test_mysum_str():
    """Test the new implmentation of mysum function."""
    expected = "abcdefg"
    result = mysum("abc", "defg")
    assert expected == result


def test_mysum_numbers():
    """Test mysym with multiple numbers"""
    expected = 6
    result = mysum(1, 2, 3)
    assert expected == result


def test_mysum_list():
    """Test  mysum with a lists"""
    expected = [1, 2, 3]
    result = mysum([1], [2, 3])
    assert expected == result


def test_alphabetize_name():
    """Tests basic last name of alphabetize_name function."""
    people = [
        {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
        {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
        {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
    ]
    expected = [
        {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
        {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
        {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
    ]
    result = alphabetize_name(people)
    assert expected == result


def test_alphabetize_name_firstname():
    """Tests of alphabetize_name function where there are the same lastname."""
    people = [
        {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
        {"first": "Donald", "last": "Putin", "email": "president@whitehouse.gov"},
        {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
    ]
    expected = [
        {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
        {"first": "Donald", "last": "Putin", "email": "president@whitehouse.gov"},
        {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
    ]
    result = alphabetize_name(people)
    assert expected == result


def test_most_repeating_word():
    """Tests most_repeating_word function."""
    expected = "elementary"
    result = most_repeating_word(["this", "is", "an", "elementary", "test", "example"])
    assert expected == result


def test_format_sort_records():
    PEOPLE = [
        ("Donald", "Trump", 7.85),
        ("Vladimir", "Putin", 3.626),
        ("Jinping", "Xi", 10.603),
    ]
    expected = "Trump      Donald      7.85\nPutin      Vladimir    3.63\nXi         Jinping    10.60"
    result = format_sort_records(PEOPLE)
    assert expected == result
