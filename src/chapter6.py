""" Code for chapter 6
"""
import operator
from typing import Callable
from random import choice

def myxml(tag_name: str, content: str='', **attributes) -> str:
    """Returns a simple xml ouput."""
    attributes = ''.join([f' {key}="{value}"' for key, value in attributes.items()])
    return f'<{tag_name}{attributes}>{content}</{tag_name}>'

def calc(math_expression: str) -> float:
    """Returns the value of a math expression that starts with math symbol"""
    operator_, value1, value2 = math_expression.split()
    operator_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }
    return operator_dict[operator_](float(value1), float(value2))

def create_password_generator(chars: str) -> Callable:
    """Creates a password generator from a set of strings."""
    def password_generator(password_len: int) -> str:
        return ''.join([choice(chars) for _ in range(password_len)])
    return password_generator
