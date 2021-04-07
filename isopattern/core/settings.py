from typing import FrozenSet

import yaml

from isopattern.core.types import (
    Element,
    Isotope
)


class Settings:

    def __init__(self, elements: FrozenSet[Element]):
        self.elements = elements

    @classmethod
    def parse_from_file(cls, path: str):

        with open(path, 'r') as file:
            raw_elements = yaml.safe_load(file)

        elements = set()
        for raw_element in raw_elements:

            isotopes = set()
            for raw_isotope in raw_element['isotopes']:
                isotopes.add(
                    Isotope(
                        name=raw_isotope['name'],
                        mass=raw_isotope['mass'],
                        abundance=raw_isotope['abundance']
                    )
                )

            elements.add(
                Element(
                    name=raw_element['name'],
                    isotopes=frozenset(isotopes)
                )
            )

        return cls(elements=frozenset(elements))
