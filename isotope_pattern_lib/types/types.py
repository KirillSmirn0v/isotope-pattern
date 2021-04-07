from typing import (
    Dict,
    FrozenSet
)


class Isotope:

    def __init__(self, name: str, mass: float, abundance: float):
        self.name = name
        self.mass = mass
        self.abundance = abundance

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

    def __init__(self, name: str, isotopes: FrozenSet[Isotope]):
        self.name = name
        self.isotopes = isotopes

    def __eq__(self, other):
        if isinstance(other, Element):
            name_equality = (self.name == other.name)
            isotopes_equality = (self.isotopes == other.isotopes)
            return name_equality and isotopes_equality

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self.isotopes))


class MolecularFormula:

    def __init__(self, name: str, elements: Dict[Element, int]):
        self.name = name
        self.elements = elements

    def __eq__(self, other):
        if isinstance(other, MolecularFormula):
            name_equality = (self.name == other.name)
            elements_equality = (self.elements == other.elements)
            return name_equality and elements_equality

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self.elements))


class IsotopeFormula:

    def __init__(self, name: str, isotopes: Dict[Isotope, int], probability: float):
        self.name = name
        self.isotopes = isotopes
        self.probability = probability

    def __eq__(self, other):
        if isinstance(other, IsotopeFormula):
            name_equality = (self.name == other.name)
            isotopes_equality = (self.isotopes == other.isotopes)
            probability_equality = (self.probability == other.probability)
            return name_equality and isotopes_equality and probability_equality
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self.isotopes, self.probability))
