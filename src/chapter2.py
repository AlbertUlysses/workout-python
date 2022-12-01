""" Code for chapter 2.
"""


def pig_latin(word: str) -> str:
    """Translates a word into piglatin"""
    if word[0] in "aeiou":
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"


def pl_sentence(sentence: str) -> str:
    """Translates a sentence that doesn't have puntuation and capitcal letters
    into pig latin.
    """
    pg_list = [pig_latin(word) for word in sentence.split()]
    return " ".join(pg_list)


def ubbi_dubbi(word: str) -> str:
    """Translates a word to ubbi dubbi."""
    ubbi_dubbi_translated_list = [
        f"ub{letter}" if letter in "aeiou" else letter for letter in word
    ]
    return "".join(ubbi_dubbi_translated_list)


def strsort(string_: str) -> str:
    """Returns the string sorted as a string"""
    return "".join(sorted(string_))
