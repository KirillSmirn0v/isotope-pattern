from typing import (
    Dict,
    List
)
from unittest.mock import patch

import pytest

from isotope_pattern_lib.core import isotope_pattern
from isotope_pattern_lib.types.types import (
    Element,
    Isotope,
    IsotopeFormula,
    MolecularFormula
)
from isotope_pattern_lib.utils import utils


# Tests for 'compute_isotope_distributions()'

@pytest.mark.parametrize(
    'isotopes,arrays,probabilities',
    [
        (['C12', 'C13'], [[10, 0], [9, 1], [8, 2], [5, 5]], [0.895, 0.100, 0.005, 0.000]),
        (['H1'], [[3]], [1.000]),
        (['O16', 'O18'], [[3, 0], [0, 3], [2, 1]], [0.994, 0.000, 0.006])
    ]
)
def test__should_produce_correct_isotope_formulas__when_function_is_called(
    isotopes: List[str],
    arrays: List[List[int]],
    probabilities: List[float],
    isotope_map: Dict[str, Isotope]
):

    element_count = sum(arrays[0])

    with patch.object(target=utils, attribute='generate_arrays_with_preserved_sum') as mock_call:
        mock_call.return_value = arrays
        new_isotopes = [isotope_map[name] for name in isotopes]
        formulas = isotope_pattern.compute_isotope_distributions(
            isotopes=new_isotopes,
            element_count=element_count
        )

    assert len(formulas) == len(arrays)

    for formula, array, probability in zip(formulas, arrays, probabilities):

        for isotope, count in formula.isotopes.items():
            assert count == array[isotopes.index(isotope.name)]

        assert formula.probability == pytest.approx(probability, abs=0.001)


# Tests for 'compute_isotope_pattern()'

def test__should_produce_correct_isotope_formulas__when_formula_is_given(
    isotope_map: Dict[str, Isotope],
    element_map: Dict[str, Element]
):

    with patch.object(isotope_pattern, 'compute_isotope_distributions') as mock_call:
        mock_call.side_effect = [
            [
                IsotopeFormula(
                    name='C12[2]',
                    isotopes={isotope_map['C12']: 2},
                    probability=0.5
                ),
                IsotopeFormula(
                    name='C12[1]C13[1]',
                    isotopes={isotope_map['C12']: 1, isotope_map['C13']: 1},
                    probability=0.25
                )
            ],
            [IsotopeFormula(name='H1[6]', isotopes={isotope_map['H1']: 6}, probability=1.0)],
            [IsotopeFormula(name='O18[1]', isotopes={isotope_map['O18']: 1}, probability=0.01)]
        ]

        pattern = isotope_pattern.compute_isotope_pattern(
            formula=MolecularFormula(
                name='C2H5OH',
                elements={
                    element_map['C']: 2,
                    element_map['H']: 6,
                    element_map['O']: 1
                }
            )
        )

        pattern = list(pattern)

        assert len(pattern) == 2
        assert pattern[0] == IsotopeFormula(
            name='C12[2]H1[6]O18[1]',
            isotopes={isotope_map['C12']: 2, isotope_map['H1']: 6, isotope_map['O18']: 1},
            probability=0.005
        )
        assert pattern[1] == IsotopeFormula(
            name='C12[1]C13[1]H1[6]O18[1]',
            isotopes={isotope_map['C12']: 1, isotope_map['C13']: 1, isotope_map['H1']: 6, isotope_map['O18']: 1},
            probability=0.0025
        )
