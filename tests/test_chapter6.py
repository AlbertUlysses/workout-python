""" Tests for chapter 6.
"""
import random as rand
from src.chapter6 import (
    myxml,
    calc,
    create_password_generator
)


def test_myxml():
    """Exercise 25: Basic test for the function myxml."""
    expected = '<foo></foo>'
    actual = myxml("foo")
    assert actual == expected

def test_myxml_content():
    """Exercise 25: Test content for function myxml."""
    expected = '<foo>bar</foo>'
    actual = myxml("foo", "bar")
    assert actual == expected

def test_myxml_attributes():
    """Exercise 25: Test setting attributes."""
    expected = '<foo a="1" b="2" c="3">bar</foo>'
    actual = myxml("foo", "bar", a=1, b=2,c=3)
    assert actual == expected

def test_calc():
    """Exercise 26: Basic test for the function calc."""
    expected = 3.0
    actual = calc('+ 1 2')
    assert actual == expected

def test_calc_sub():
    """Exercise 26: Basic test for the function calc."""
    expected = 3.0
    actual = calc('- 5 2')
    assert actual == expected

def test_calc_div():
    """Exercise 26: Basic test for the function calc."""
    expected = 3.0
    actual = calc('/ 9 3')
    assert actual == expected

def test_create_password_generator():
    """Exercise 27: Basic test for function create_password_gen."""
    rand.seed(10)
    expected = "dab"
    abc_password_gen = create_password_generator("abd")
    assert abc_password_gen(3) == expected
