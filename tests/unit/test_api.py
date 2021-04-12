from unittest.mock import patch

from isotope_pattern_lib import api
from isotope_pattern_lib.core import isotope_pattern
from isotope_pattern_lib.types.settings import Settings
from isotope_pattern_lib.types.types import (
    Isotope,
    IsotopeFormula
)


def test__should_initialize_default_parser__when_set_parser_is_not_called():

    element_names = set(api.parser.valid_elements.keys())

    expected_names = {'C', 'H', 'O', 'N'}

    assert len(element_names.intersection(expected_names)) == len(expected_names)
    assert len(expected_names.intersection(element_names)) == len(expected_names)


def test__should_substitute_existing_parser__when_set_parser_is_called():

    with patch.object(
        target=Settings,
        attribute='parse_from_file',
    ) as mock_call:
        mock_call.return_value = Settings(elements=frozenset())
        api.set_parser(config_path='')

    assert len(api.parser.valid_elements.keys()) == 0


def test__should_make_function_calls__when_compute_isotope_pattern_is_called():

    isotope_formulas = [
        IsotopeFormula(
            name='formula 1',
            isotopes={Isotope(name='', mass=2.0, abundance=0.0): 1},
            probability=0.0
        ),
        IsotopeFormula(
            name='formula 2',
            isotopes={Isotope(name='', mass=1.0, abundance=0.0): 1},
            probability=0.0
        )
    ]

    with patch.object(
        target=api.parser,
        attribute='parse'
    ) as mock_parse_call:
        with patch.object(
            target=isotope_pattern,
            attribute='compute_isotope_pattern'
        ) as mock_compute_isotope_pattern_call:
            mock_compute_isotope_pattern_call.return_value = isotope_formulas

            patterns = api.compute_isotope_pattern(formula_string='')

            mock_parse_call.assert_called_once()
            mock_compute_isotope_pattern_call.assert_called_once()

    assert len(patterns) == len(isotope_formulas)
    assert patterns == list(reversed(isotope_formulas))
