""" Tests for chapter 10.
"""
from src.chapter10 import (
    MyEnumerate,
    Circle,
    get_directory_line,
    elapsed_since,
    mychain
)


def test_myenumerate(capsys):
    """Exercise 46: Basic test for MyEnumerate class."""
    for index, letter in MyEnumerate('abc'):
        print(f"{index}: '{letter}'")
    output, _ = capsys.readouterr()
    assert "0: 'a'" in output
    assert "1: 'b'" in output
    assert "2: 'c'" in output

def test_circle(capsys):
    """Exercise 47: Basic test for the class Circle."""
    c = Circle('abc', 5)
    print(list(c))
    output, _ = capsys.readouterr()
    assert "a" in output
    assert "b" in output
    assert "c" in output

def test_get_directory_line():
    """Exercise 48: Basic test for the generator get_directory_line"""
    expected_1 = 'there.\n'
    expected_2 = 'hello.\n'
    generator_ = get_directory_line('tests/files/generators')
    actual_1 = next(generator_)
    actual_2 = next(generator_)
    assert actual_1 == expected_1
    assert actual_2 == expected_2

def test_elapsed_since():
    """Exercise 49: Basic test for the generator elapsed_since not testing time.
    """
    expected_1 = 'a'
    expected_time_1 = 0.0
    expected_2 = 'b'
    generator_ = elapsed_since('abc')
    actual_1, actual_time_1= next(generator_)
    actual_2, _ = next(generator_)
    assert actual_1 == expected_1
    assert actual_time_1 == expected_time_1
    assert actual_2 == expected_2

def test_mychain():
    """Exercise 50: Basic test for the generator mychain.
    """
    expected_1 = 'a'
    expected_2 = 'b'
    expected_3 = 1
    generator_ = mychain('ab', [1,2])
    actual_1 =next(generator_)
    actual_2 = next(generator_)
    actual_3 = next(generator_)
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
