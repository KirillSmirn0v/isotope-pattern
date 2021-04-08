from os import path
from typing import Dict

import pytest

from isotope_pattern_lib.core.formula_parser import MolecularFormulaParser
from isotope_pattern_lib.types.settings import Settings
from isotope_pattern_lib.types.types import Element


config_path = path.join('tests', 'data', 'unit', 'config_good.yaml')


@pytest.mark.parametrize('settings', [{'file_path': config_path}], indirect=True)
def test__should_parse_formula_correctly__when_valid_string_is_given(
    settings: Settings,
    element_map: Dict[str, Element]
):

    parser = MolecularFormulaParser(settings=settings)

    formula_raw = 'C2H5OH'
    formula = parser.parse(raw_string=formula_raw)

    assert formula.name == formula_raw

    elements = formula.elements

    assert len(elements) == 3

    assert element_map['C'] in elements
    assert element_map['H'] in elements
    assert element_map['O'] in elements

    assert elements[element_map['C']] == 2
    assert elements[element_map['O']] == 1
    assert elements[element_map['H']] == 6


@pytest.mark.parametrize('settings', [{'file_path': config_path}], indirect=True)
def test__should_raise_error__when_invalid_string_is_given(
    settings: Settings,
    element_map: Dict[str, Element]
):

    parser = MolecularFormulaParser(settings=settings)

    formula_raw = 'NH4'
    with pytest.raises(ValueError):
        parser.parse(raw_string=formula_raw)
