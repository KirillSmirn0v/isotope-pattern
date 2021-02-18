import re

from isopattern.core.settings import Settings
from isopattern.core.types import MolecularFormula


class MolecularFormulaParser:

    pattern = re.compile(r'([A-Z][a-z]?)(\d*)')

    def __init__(self, settings: Settings):
        self.valid_elements = {element.name: element for element in settings.elements}

    def parse(self, raw_string: str) -> MolecularFormula:

        matches = MolecularFormulaParser.pattern.findall(raw_string)

        element_counts = dict()
        for match in matches:
            if match[0] in self.valid_elements:
                element = self.valid_elements[match[0]]
                count = 1 if match[1] == '' else int(match[1])
                if element in element_counts:
                    element_counts[element] += count
                else:
                    element_counts[element] = count
            else:
                raise ValueError(f"'{match[0]}' was not found among provided element list")

        return MolecularFormula(name=raw_string, elements=element_counts)
