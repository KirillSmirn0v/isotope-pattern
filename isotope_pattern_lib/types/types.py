from typing import (
    Dict,
    List
)


class Isotope:

    def __init__(self, name: str, mass: float, abundance: float):
        self.name = name
        self.mass = mass
        self.abundance = abundance

    def __repr__(self):
        return (
            f'{self.__class__.__name__}'
            f'(name={self.name}, mass={round(self.mass, 3)}, abundance={round(self.abundance, 3)})'
        )

    def __eq__(self, other):
        if isinstance(other, Isotope):
            name_equality = (self.name == other.name)
            mass_equality = (self.mass == other.mass)
            abundance_equality = (self.abundance == other.abundance)
            return name_equality and mass_equality and abundance_equality
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self.mass, self.abundance))


class Element:

    def __init__(self, name: str, isotopes: List[Isotope]):
        self.name = name
        self.isotopes = isotopes
        self._isotopes = frozenset(isotopes)

    def __repr__(self):
        isotope_names = [isotope.name for isotope in self.isotopes]
        return f'{self.__class__.__name__}(name={self.name}, isotopes={",".join(isotope_names)})'

    def __eq__(self, other):
        if isinstance(other, Element):
            name_equality = (self.name == other.name)
            isotopes_equality = (self._isotopes == other._isotopes)
            return name_equality and isotopes_equality
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self._isotopes))


class MolecularFormula:

    def __init__(self, name: str, elements: Dict[Element, int]):
        self.name = name
        self.elements = elements

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name})'

    def __eq__(self, other):
        if isinstance(other, MolecularFormula):
            name_equality = (self.name == other.name)
            elements_equality = (self.elements == other.elements)
            return name_equality and elements_equality
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class IsotopeFormula:

    def __init__(self, name: str, isotopes: Dict[Isotope, int], probability: float):
        self.name = name
        self.isotopes = isotopes
        self.probability = probability
        self.mass = self.compute_mass()

    def __repr__(self):
        return (
            f'{self.__class__.__name__}'
            f'(name={self.name}, mass={round(self.mass, 3)}, probability={round(self.probability, 3)})'
        )

    def compute_mass(self) -> float:
        mass = 0.0
        for isotope, count in self.isotopes.items():
            mass += isotope.mass * count
        return mass

    def __eq__(self, other):
        if isinstance(other, IsotopeFormula):
            name_equality = (self.name == other.name)
            isotopes_equality = (self.isotopes == other.isotopes)
            probability_equality = (self.probability == other.probability)
            return name_equality and isotopes_equality and probability_equality
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
