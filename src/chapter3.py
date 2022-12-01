""" Solutions for chapter 3.
"""
from typing import List
from collections import Counter


def firstlast(iterable_object):
    return iterable_object[:1] + iterable_object[-1:]


def mysum(*iterable_object):
    """mysum implementation that intakes multiple types."""
    if not iterable_object:
        return iterable_object
    combined_object = iterable_object[0]
    for value in iterable_object[1:]:
        combined_object += value
    return combined_object


def alphabetize_name(PEOPLE):
    """Sorts a dictionary that has a first and last name by last,then first"""
    """
    sorted_names = sorted([(person['last'], person['first']) for person in PEOPLE])
    sorted_dict_ = []
    for names in sorted_names:
        for person in PEOPLE:
            if (person['last'],person['first']) == names:
                sorted_dict_.append(person)
    return sorted_dict_
    """
    return sorted(PEOPLE, key=lambda x: (x["last"], x["first"]))


def most_repeating_word(list_of_string: List[str]) -> str:
    """returns a word that has the most repeated of one letter"""
    final_word = ""
    most_letter = 0
    for word in list_of_string:
        sorted_counter = Counter(word).most_common(1)[0]
        if sorted_counter[1] > most_letter:
            most_letter = sorted_counter[1]
            final_word = word
    return final_word


def format_sort_records(people: list) -> str:
    """Retuns a string with first,last and time formatted."""
    formatted_list = [
        f"{person[1]:10} {person[0]:10} {person[2]:5.2f}" for person in people
    ]
    return "\n".join(formatted_list)
