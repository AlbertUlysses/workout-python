""" Tests for chapter 7.
"""
from io import StringIO
from src.chapter7 import (
    join_numbers,
    sum_numbers,
    flatten,
    pl_file,
    flip_dict,
    transform_values,
    get_sv,
    get_alpha_dict,
    gematria_for
)


def test_join_numbers():
    """Exercise 28: Basic test for the function join_numbers."""
    expected = '0,1,2,3,4,5'
    actual = join_numbers(6)
    assert actual == expected

def test_sum_numbers():
    """Exercise 29: Basic test for the function sum_numbers."""
    expected = 100
    actual = sum_numbers('10 abc 20 de44 30 55fg 40')
    assert actual == expected

def test_flatten():
    """Exercise 30: Basic test for the function flatten."""
    expected = [1, 2, 3, 4]
    actual = flatten([[1, 2], [3, 4]])
    assert actual == expected

def test_pl_file():
    """Exercise 31: Basic test for the function pg_file."""
    expected = "histay isway away esttay ranslationtay\nhistay isway away esttay ranslationtay"
    actual = pl_file('tests/files/pl_test.txt')
    assert actual == expected

def test_flip_dict():
    """Exercise 32: Basic test for the function file_dict."""
    expected = {
        1: 'a',
        2: 'b',
        3: 'c'
    }
    actual = flip_dict(
        {
            'a': 1,
            'b': 2,
            'c': 3
        }
    )
    assert actual == expected

def test_transform_values():
    """Exercise 33: Basic test for the function transform_values."""
    expected = {
        'a': 1,
        'b': 4,
        'c': 9
    }
    actual = transform_values(
        lambda x: x*x,
        {
            'a': 1,
            'b': 2,
            'c': 3
        }
    )
    assert actual == expected

def test_get_sv():
    """Exercise 34: Basic test for the function get_sv."""
    expected = {"haeiou", "beaoui"}
    actual = get_sv('tests/files/sv_test.txt')
    assert actual == expected

def test_get_alpha_dict():
    """Exercise 35A: Basic test for the function get_alpha_dict."""
    expected = {
        'a': 1,
        'b': 2
    }
    actual = get_alpha_dict(2)
    assert actual == expected

def test_gematria_for():
    """Exercise 35B: Basic test for the function gematria_for."""
    expected = 3
    actual = gematria_for('ab')
    assert actual == expected

def test_gematria_equal_words():
    """Exercise 35B: Did not create this function because it's dumb"""
    pass
