""" Code for chapter 9
"""
from typing import List
from dataclasses import dataclass, field

class Scoop:
    def __init__(self, flavor: str):
        self.flavor = flavor

class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)

    def add_scoops(self, *scoops: Scoop):
        for scoop in scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scoop)

class BigBowl(Bowl):
    max_scoops = 5

class FlexibleDict(dict):
    def __missing__(self, key):
        try:
            return self.__getitem__(int(key))
        except:
            raise KeyError()

@dataclass(frozen=True)
class Animal:
    legs: int
    species: str
    color: str

    def __repr__(self) -> str:
        return f'{self.color.capitalize()} {self.species}, {self.legs} legs'

@dataclass(frozen=True, repr=False, init=False)
class Sheep(Animal):
    def __init__(self, color):
        super().__init__(
            legs=4,
            species=self.__class__.__name__.lower(),
            color=color
        )

@dataclass(frozen=True, repr=False, init=False)
class Parrot(Animal):
    def __init__(self, color):
        super().__init__(
            legs=2,
            species=self.__class__.__name__.lower(),
            color=color
        )

@dataclass(frozen=True, repr=False, init=False)
class Wolf(Animal):
    def __init__(self, color):
        super().__init__(
            legs=4,
            species=self.__class__.__name__.lower(),
            color=color
        )

@dataclass(frozen=True, repr=False, init=False)
class Snake(Animal):
    def __init__(self, color):
        super().__init__(
            legs=0,
            species=self.__class__.__name__.lower(),
            color=color
        )
@dataclass
class Cage:
    id: int
    cage_animals: List[Animal] = field(default_factory=list)

    def add_animals(self, *animals):
        self.cage_animals.extend(animals)

    def __repr__(self) -> str:
        return (
            f"Cage ID: {self.id}, "
            "Cage contains: "
            f"{', '.join(str(animal) for animal in  self.cage_animals)}"
        )

@dataclass
class Zoo:
    cages: List[Cage] = field(default_factory=list)

    def add_cages(self, *cages) -> None:
        self.cages.extend(cages)

    def animals_by_color(self, color: str) -> List[Animal]:
        return [
            animal
            for cage in self.cages
            for animal in cage.cage_animals
            if animal.color.lower() == color.lower()
        ]

    def animals_by_legs(self, legs: int) -> List[Animal]:
        return [
            animal
            for cage in self.cages
            for animal in cage.cage_animals
            if animal.legs == legs
        ]

    def number_of_legs(self) -> int:
        return sum(
            animal.legs
            for cage in self.cages
            for animal in cage.cage_animals
        )

    def __repr__(self):
        return '\n'.join(str(cage) for cage in self.cages)

def create_scoops(*flavors: Scoop) -> list:
    """Returns a list of flavors from a Scoop"""
    scoops = [Scoop(flavor) for flavor in flavors]
    return [scoop.flavor for scoop in scoops]
