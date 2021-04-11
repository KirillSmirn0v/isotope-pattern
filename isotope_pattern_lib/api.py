import os
import pkg_resources
from typing import List

from isotope_pattern_lib.core import isotope_pattern
from isotope_pattern_lib.core.formula_parser import MolecularFormulaParser
from isotope_pattern_lib.types.settings import Settings
from isotope_pattern_lib.types.types import IsotopeFormula


parser = MolecularFormulaParser(
    settings=Settings.parse_from_file(pkg_resources.resource_filename(
        'isotope_pattern_lib',
        os.path.join('resources', 'config.yaml')
    ))
)


def set_parser(config_path: str):

    global parser
    settings = Settings.parse_from_file(path=config_path)
    parser = MolecularFormulaParser(settings=settings)


def compute_isotope_pattern(formula_string: str) -> List[IsotopeFormula]:

    global parser
    formula = parser.parse(raw_string=formula_string)

    patterns = isotope_pattern.compute_isotope_pattern(formula=formula)
    return sorted(patterns, key=lambda x: x.mass)
