""" Tests for chapter 5.
"""
import os
from pathlib import Path

from src.chapter5 import (
    get_final_line,
    passwrd_to_dict,
    word_count,
    find_longest_word,
    find_all_longest_words,
    passwrd_to_csv,
    calculate_score,
    print_scores,
    reverse_lines,
)


def test_get_final_line():
    """Chpater 18: Tests the function get_final_line."""
    expected = "This is the last line."
    actual = get_final_line("tests/files/fake.txt")
    assert actual == expected


def test_passwrd_to_dict():
    """Exercise 19: Test basic the function password_to_dict."""
    expected = {"nobody": "-2", "root": "0"}
    actual = passwrd_to_dict("tests/files/passwrd.txt")
    assert actual == expected


def test_word_count():
    """Exercise 20: basic test for word_count."""
    expected = "This file has: 158 characters, 28 words, 20 unique words, and 6 lines"
    actual = word_count("tests/files/wcfile.txt")
    assert actual == expected


def test_find_longest_word():
    """Exercise 21: basic test for find_longest_word."""
    expected = "first"
    actual = find_longest_word("tests/files/fake.txt")
    assert actual == expected


def test_find_all_longest_words():
    """Exercise 21: basic test for find_all_longest_words."""
    expected = {"wcfile.txt": "referential", "fake.txt": "first"}
    actual = find_all_longest_words("tests/files/multiple_files")
    assert actual == expected


def test_passwrd_to_csv():
    """Exercise 22: tests that passwrd_to_csv creates a new file and content"""
    expected_file_path = "tests/files/passwrd_to_csv.csv"
    expected = "nobody\t-2\nroot\t0\n"
    passwrd_to_csv("tests/files/passwrd2.txt", "tests/files/passwrd_to_csv.csv")
    with open("tests/files/passwrd_to_csv.csv", "r") as f:
        actual = f.read()
    assert Path(expected_file_path).exists()
    assert actual == expected


def test_calculate_score():
    list_of_classes = [
        {"math": 90, "literature": 98, "science": 97},
        {"math": 65, "literature": 79, "science": 85},
        {"math": 78, "literature": 83, "science": 75},
        {"math": 92, "literature": 78, "science": 85},
        {"math": 100, "literature": 80, "science": 90},
    ]
    expected_min = 75
    expected_max = 97
    expected_avg = 86.4
    actual_min, actual_max, actual_avg = calculate_score(list_of_classes, "science")
    assert actual_min == expected_min
    assert actual_max == expected_max
    assert actual_avg == expected_avg


def test_print_scores(capsys):
    """Exercise 23: basic test for print_scores."""
    expected = "math: min 65, max 100, average 85\nliterature: min 78, max 98, average 83.6\nscience: min 75, max 97, average 86.4"
    print_scores("tests/files/9a.json")
    output, _ = capsys.readouterr()
    assert expected in output


def test_reverse_lines(tmp_path):
    """Excercise 24: Base test for reverse_lines."""
    file_path = tmp_path / "output.txt"
    expected = "fed cba\nlkj ihg\n"
    reverse_lines("tests/files/reverse.txt", file_path)
    assert file_path.read_text() == expected
