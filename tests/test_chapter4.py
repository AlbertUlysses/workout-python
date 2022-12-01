""" Tests for Chapter 4.
"""
from io import StringIO

from src.chapter4 import restaurant, get_rainfall, dict_diff, how_many_different_numbers


def test_restaurant(capsys, monkeypatch):
    """Test for the function restuaurant."""
    monkeypatch.setattr("sys.stdin", StringIO("sandwich\ntea\nelephant\n\n"))
    restaurant()
    output, _ = capsys.readouterr()
    assert "Elephant is not on the Menu." in output
    assert "Your Total is 17" in output


def test_get_rainfall(capsys, monkeypatch):
    """Test the function get_rainfall."""
    monkeypatch.setattr(
        "sys.stdin", StringIO("Boston\n10\nboston\n10\nSan jose\n10\n\n")
    )
    get_rainfall()
    output, _ = capsys.readouterr()
    assert "Boston: 20" in output
    assert "San jose: 10" in output


def test_dictdiff_same_keys_values():
    """Tests when two dicts have the same values."""
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 1, "b": 2, "c": 3}
    expected = {}
    actual = dict_diff(d1, d2)
    assert actual == expected


def test_dictdiff_diff_keys():
    """Tests when two dicts have the different values."""
    d1 = {"a": 1, "b": 2, "d": 3}
    d2 = {"a": 1, "b": 2, "c": 4}
    expected = {"c": [None, 4], "d": [3, None]}
    actual = dict_diff(d1, d2)
    assert actual == expected


def test_dictdiff_diff_values():
    """Tests when two dicts have the different values."""
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 1, "b": 2, "c": 4}
    expected = {"c": [3, 4]}
    actual = dict_diff(d1, d2)
    assert actual == expected


def test_how_many_different_numbers():
    """Test that passes a basic list with some repeats."""
    test_list = [1, 2, 3, 1, 2, 3, 4, 1]
    expected = 4
    actual = how_many_different_numbers(test_list)
    assert actual == expected
