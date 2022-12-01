""" Tests for chapter 9.
"""
from io import StringIO
from src.chapter9 import (
    create_scoops,
    Scoop,
    Bowl,
    BigBowl,
    FlexibleDict,
    Sheep,
    Snake,
    Wolf,
    Parrot,
    Cage,
    Zoo
)

import pytest

@pytest.fixture
def zoo():
    test_cage1 = Cage(1)
    test_cage2 = Cage(2)
    test_wolf1 = Wolf("Grey")
    test_sheep1 = Sheep("White")
    test_wolf2 = Wolf("White")
    test_sheep2 = Sheep("Black")
    test_cage1.add_animals(test_wolf1, test_sheep1)
    test_cage2.add_animals(test_wolf2, test_sheep2)
    test_zoo = Zoo()
    test_zoo.add_cages(test_cage1, test_cage2)
    return test_zoo

def test_create_scoops():
    """Exercise 38: Basic test for the function create_scoops."""
    expected = ['chocolate', 'vanilla', 'persimmon']
    actual = create_scoops('chocolate', 'vanilla', 'persimmon')
    assert actual == expected

def test_add_scope(capsys):
    """Exercise 39: Basic test for checking output of a Bowl."""
    scoop_1 = Scoop('chocolate')
    scoop_2 = Scoop('vanilla')
    scoop_3 = Scoop('persimmon')
    test_bowl = Bowl()
    test_bowl.add_scoops(scoop_1, scoop_2)
    test_bowl.add_scoops(scoop_3)
    print(test_bowl)
    output, _ = capsys.readouterr()
    assert "chocolate" in output
    assert "vanilla" in output
    assert "persimmon" in output

def test_max_scoops(capsys):
    """Exercise 40: Basic test for checking max scoops for Bowl."""
    scoop_1 = Scoop('chocolate')
    scoop_2 = Scoop('vanilla')
    scoop_3 = Scoop('persimmon')
    scoop_4 = Scoop('Oreo')
    test_bowl = Bowl()
    test_bowl.add_scoops(scoop_1, scoop_2)
    test_bowl.add_scoops(scoop_3, scoop_4)
    print(test_bowl)
    output, _ = capsys.readouterr()
    assert "chocolate" in output
    assert "vanilla" in output
    assert "persimmon" in output
    assert "Oreo" not in output

def test_max_scoops_big_bowl(capsys):
    """Exercise 41: Basic test for checking max scoops for BigBowl."""
    scoop_1 = Scoop('chocolate')
    scoop_2 = Scoop('vanilla')
    scoop_3 = Scoop('persimmon')
    scoop_4 = Scoop('Oreo')
    scoop_5 = Scoop('Strawberry')
    scoop_6 = Scoop('Pecan')
    test_bowl = BigBowl()
    test_bowl.add_scoops(scoop_1, scoop_2, scoop_3, scoop_4, scoop_5, scoop_6)
    print(test_bowl)
    output, _ = capsys.readouterr()
    assert "chocolate" in output
    assert "vanilla" in output
    assert "persimmon" in output
    assert "Oreo" in output
    assert "Strawberry" in output
    assert "Pecan" not in output

def test_flexible_dict():
    """Exercise 42: Basic test for checking FlexibleDict retrieving."""
    expected = 'a'
    dict_ = FlexibleDict()
    dict_[1] = 'a'
    actual = dict_['1']
    assert actual == expected

def test_flexible_dict_error():
    """Exercise 42: Error test for checking FlexibleDict retrieving."""
    dict_ = FlexibleDict()
    dict_[1] = 'a'
    actual = dict_['1']
    with pytest.raises(KeyError):
        dict_[2]

def test_sheep(capsys):
    """Exercise 43: Basic test for checking output of a sheep."""
    test_sheep = Sheep("white")
    print(test_sheep)
    output, _ = capsys.readouterr()
    assert "White sheep, 4 legs" in output

def test_wolf(capsys):
    """Exercise 43: Basic test for checking output of a wolf."""
    test_wolf = Wolf("Grey")
    print(test_wolf)
    output, _ = capsys.readouterr()
    assert "Grey wolf, 4 legs" in output

def test_snake(capsys):
    """Exercise 43: Basic test for checking output of a snake."""
    test_snake = Snake("Green")
    print(test_snake)
    output, _ = capsys.readouterr()
    assert "Green snake, 0 legs" in output

def test_parrot(capsys):
    """Exercise 43: Basic test for checking output of a parrot."""
    test_parrot = Parrot("Red")
    print(test_parrot)
    output, _ = capsys.readouterr()
    assert "Red parrot, 2 legs" in output

def test_cage(capsys):
    """Exercise 44: Basic test for Cage class."""
    test_cage = Cage(1)
    test_wolf = Wolf("Grey")
    test_sheep = Sheep("White")
    test_cage.add_animals(test_wolf, test_sheep)
    print(test_cage)
    output, _ = capsys.readouterr()
    assert "Cage ID: 1, Cage contains: Grey wolf, 4 legs, White sheep, 4 legs" in output

def test_zoo(capsys, zoo):
    """Exercise 45: Basic test for Zoo class print."""
    print(zoo)
    output, _ = capsys.readouterr()
    assert "Cage ID: 1, Cage contains: Grey wolf, 4 legs, White sheep, 4 legs" in output
    assert "Cage ID: 2, Cage contains: White wolf, 4 legs, Black sheep, 4 legs" in output

def test_zoo_animals_by_color(zoo):
    """Exercise 45: Basic test for Zoo class animals by colors method."""
    expected = [Sheep('White'), Wolf('White')]
    actual = zoo.animals_by_color('white')
    assert actual == expected

def test_zoo_animals_by_color(zoo):
    """Exercise 45: Basic test for Zoo class animals by legs method."""
    expected = [Wolf('Grey'), Sheep('White'), Wolf('White'), Sheep('Black')]
    actual = zoo.animals_by_legs(4)
    assert actual == expected

def test_zoo_number_of_legs(zoo):
    """Exercise 45: Basic test for Zoo class animals by legs method."""
    expected = 16
    actual = zoo.number_of_legs()
    assert actual == expected
