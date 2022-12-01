""" Tests for chapter1.
"""
import random
import pytest
import sys
from io import StringIO

from chapter1 import guessing_game, my_sum, run_timing, hex_output


def test_guessing_game(capsys, monkeypatch):
    """tests guessing game will return "Too low" when the number is higher."""
    random.seed(10)
    monkeypatch.setattr("sys.stdin", StringIO("5\n80\n74\n"))
    guessing_game()
    output, _ = capsys.readouterr()
    assert "Too low" in output
    assert "Too High" in output
    assert "Just right" in output


def test_my_sum():
    """Tests my_sum function."""
    expected = 5
    assert my_sum(1, 2, 2) == expected


def test_run_timing(capsys, monkeypatch):
    """Tests run_timing function."""
    monkeypatch.setattr("sys.stdin", StringIO("10\n20\n15\n\n"))
    run_timing()
    output, _ = capsys.readouterr()
    assert "Average of 15.00, over 3 runs" in output


def test_hex_output(capsys, monkeypatch):
    """Tests hex_output function."""
    monkeypatch.setattr("sys.stdin", StringIO("50\n"))
    output = hex_output()
    assert output == 80
