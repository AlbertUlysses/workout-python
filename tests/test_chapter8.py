""" Tests for chapter 8.
"""
from io import StringIO

from src.freedonia import calculate_tax
from src.menu import menu


def test_calculate_tax():
    """Exercise 36: Basic test for the function calculate_tax."""
    expected = 125.00
    actual = calculate_tax(500, 'Harpo', 12)
    assert actual == expected

def test_menu(capsys, monkeypatch):
    """Exercise 37: Basic test for the function menu."""
    def funct_A():
        """for testing excersice 37"""
        return 'A'
    monkeypatch.setattr(
        "sys.stdin", StringIO("q\na\n")
    )
    menu(a=funct_A)
    output, _ = capsys.readouterr()
    assert "'q' is not a Valid Keyword." in output
    assert "A" in output
