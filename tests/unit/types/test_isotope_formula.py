from typing import (
    Dict,
    List,
    Tuple
)

import pytest

from isotope_pattern_lib.types.types import (
    Isotope,
    IsotopeFormula
)


isotope_params = {
    'C12': (12.0, 0.989),
    'C13': (13.0033548, 0.011),
    'H1': (1.0078250, 1.000),
    'O16': (15.9949146, 0.998),
    'O18': (17.9991596, 0.002)
}


formula_params = [
    ('C12[1]H1[4]', {'C12': 1, 'H1': 4}),
    ('C12[1]C13[1]H1[6]O16[1]', {'C12': 1, 'C13': 1, 'H1': 6, 'O16': 1}),
    ('C12[3]C13[3]H1[12]O16[3]O18[3]', {'C12': 3, 'C13': 3, 'H1': 12, 'O16': 3, 'O18': 3})
]


@pytest.mark.parametrize(
    'mass_counts,expected_mass',
    [
        ([(1.0, 1), (2.0, 2)], 5.0),
        ([(2.0, 1), (1.0, 2)], 4.0),
        ([(1.0, 0), (2.0, 0), (3.0, 0)], 0.0)
    ]
)
def test__should_compute_correct_mass__when_isotope_formula_instance_is_created(
    mass_counts: List[Tuple[float, int]],
    expected_mass: float
):

    formula = IsotopeFormula(
        name='',
        isotopes={Isotope(name='', mass=mass, abundance=0.0): count for mass, count in mass_counts},
        probability=0.0
    )

    assert formula.mass == expected_mass


@pytest.mark.parametrize('name,isotope_counts', formula_params)
def test__should_affirm_instance_equality__when_isotope_formula_instances_have_same_fields(
    name: str,
    isotope_counts: Dict[str, int]
):

    formula1 = IsotopeFormula(
        name=name,
        isotopes={
            Isotope(
                name=name,
                mass=isotope_params[name][0],
                abundance=isotope_params[name][1]
            ): count for name, count in isotope_counts.items()
        },
        probability=0.0,
    )

    formula2 = IsotopeFormula(
        name=name,
        isotopes={
            Isotope(
                name=name,
                mass=isotope_params[name][0],
                abundance=isotope_params[name][1]
            ): count for name, count in isotope_counts.items()
        },
        probability=0.0,
    )

    assert formula1 == formula2


@pytest.mark.parametrize('name,isotope_counts', formula_params)
def test__should_affirm_instance_inequality__when_isotope_formula_instances_have_different_fields(
    name: str,
    isotope_counts: Dict[str, int]
):

    formula1 = IsotopeFormula(
        name=name,
        isotopes={
            Isotope(
                name=name,
                mass=isotope_params[name][0],
                abundance=isotope_params[name][1]
            ): count for name, count in isotope_counts.items()
        },
        probability=0.0,
    )

    formula2 = IsotopeFormula(
        name='C12[1]H1[4]',
        isotopes={
            Isotope(
                name=name,
                mass=isotope_params[name][0],
                abundance=isotope_params[name][1]
            ): count for name, count in isotope_counts.items()
        },
        probability=0.1,
    )

    assert formula1 != formula2


@pytest.mark.parametrize('name,isotope_counts', formula_params)
def test__should_affirm_instance_inequality__when_comparison_with_another_class(
    name: str,
    isotope_counts: Dict[str, int]
):

    formula = IsotopeFormula(
        name=name,
        isotopes={
            Isotope(
                name=name,
                mass=isotope_params[name][0],
                abundance=isotope_params[name][1]
            ): count for name, count in isotope_counts.items()
        },
        probability=0.0,
    )

    assert formula != 1
    assert formula != 'str'
    assert formula != [1, 2, 3]


@pytest.mark.parametrize('name,isotope_counts', formula_params)
def test__should_return_correct_string__when_string_representation_is_invoked(
    name: str,
    isotope_counts: Dict[str, int]
):

    formula = IsotopeFormula(
        name=name,
        isotopes={
            Isotope(
                name=name,
                mass=isotope_params[name][0],
                abundance=isotope_params[name][1]
            ): count for name, count in isotope_counts.items()
        },
        probability=0.25,
    )

    expected_string = (
        f'IsotopeFormula'
        f'(name={name}, mass={round(formula.mass, 3)}, probability={round(formula.probability, 3)})'
    )
    assert str(formula) == expected_string
