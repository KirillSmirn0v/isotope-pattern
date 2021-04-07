import os
import pkg_resources
from typing import List

from isopattern.core import pattern
from isopattern.core.parser import MolecularFormulaParser
from isopattern.core.settings import Settings
from isopattern.core.types import IsotopeFormula


parser = MolecularFormulaParser(
    settings=Settings.parse_from_file(pkg_resources.resource_filename(
        'isopattern',
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

    return pattern.compute(formula=formula)
