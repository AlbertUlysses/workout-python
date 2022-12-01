""" Code for chapter 10
"""
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any

@dataclass
class MyEnumerateIterator:
    iter_: Iterable
    index: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iter_):
            raise StopIteration
        value = self.index, self.iter_[self.index]
        self.index += 1
        return value

@dataclass
class MyEnumerate:
    iter_: Iterable

    def __iter__(self):
        return MyEnumerateIterator(self.iter_)

@dataclass
class CircleIterator:
    iter_: Iterable
    max_: int
    index: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max_:
            raise StopIteration
        value = self.iter_[self.index % len(self.iter_)]
        self.index += 1
        return value

@dataclass
class Circle:
    iter_: Iterable
    max_: int

    def __iter__(self):
        return CircleIterator(self.iter_, self.max_)

def get_directory_line(directory_path: str) -> str:
    """Yields a line for each file in the given directory."""
    for file_ in Path(directory_path).glob("**/*"):
        try:
            with open(str(file_), 'r') as file_:
                yield file_.readline()
        except OSError:
            pass

def elapsed_since(iterable_: Iterable) -> tuple:
    """Yields the most current time and iterable value of given iterable."""
    last_time = None
    for item in iterable_:
        current_time = perf_counter()
        delta = (
            current_time - last_time
            if last_time
            else current_time - current_time
        )
        last_time = current_time
        yield item, delta

def mychain(*iterable_: Iterable) -> Any:
    """Yields a line for each file in the given directory."""
    for items in iterable_:
        for item in items:
            yield item
