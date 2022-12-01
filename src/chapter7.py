""" Code for chapter 7
"""
import string
from typing import List, Callable

from src.chapter2 import pl_sentence

def join_numbers(range_: int) -> str:
    """Returns a list of numbers for given range as a string."""
    return ','.join(str(num) for num in range(range_))

def sum_numbers(long_string: str) -> int:
    """Returns total for all the numbers in the string."""
    return sum(int(num) for num in long_string.split() if num.isnumeric())

def flatten(list_of_lists: List[list])-> list:
    """Returns a flatten from a 2 dim list."""
    return [value2 for value1 in list_of_lists for value2 in value1]

def pl_file(file_name: str) -> str:
    """Returns all of a file's content as piglatin"""
    with open(file_name, "r", encoding="utf-8") as file_:
        return '\n'.join(pl_sentence(line_) for line_ in file_)

def flip_dict(dict_: dict) -> dict:
    """Returns the given dict with the values and keys flipped."""
    return {value: key for key, value in dict_.items()}

def transform_values(function_: Callable, dict_: dict) -> dict:
    """Returns the given dict with the values transformed by the function"""
    return {key: function_(value) for key, value in dict_.items()}

def get_sv(file_name: str) -> set:
    """Returns a set of a file's content that has all the of vowels."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(file_name, "r", encoding="utf-8") as file_:
        return {line_.strip() for line_ in file_ if vowels.issubset(set(line_))}

def get_alpha_dict(number_of_letters: int) -> dict:
    """Returns a dict with the alphabet depending on the given number"""
    return {
        value: index
        for index, value in enumerate(
            string.ascii_lowercase[:number_of_letters], 1
        )
    }

def gematria_for(word: str) -> int:
    """Returns a gematria_score word"""
    alphabet = get_alpha_dict(26)
    return sum(alphabet[letter] for letter in word)

def gematria_equal_words():
    """Did not create this function because it's dumb excersise."""
    pass
