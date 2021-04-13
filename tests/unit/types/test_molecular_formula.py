from typing import Dict

import pytest

from isotope_pattern_lib.types.types import (
    Element,
    Isotope,
    MolecularFormula
)


element_params = {
    'C': [('C12', 12.0, 0.989), ('C13', 13.0033548, 0.011)],
    'H': [('H1', 1.0078250, 1.000)],
    'O': [('O16', 15.9949146, 0.998), ('O18', 17.9991596, 0.002)]
}


formula_params = [
    ('CH4', {'C': 1, 'H': 4}),
    ('C2H5OH', {'C': 2, 'H': 6, 'O': 1}),
    ('C6H12O6', {'C': 6, 'H': 12, 'O': 6})
]


@pytest.mark.parametrize('name,element_counts', formula_params)
def test__should_affirm_instance_equality__when_molecular_formula_instances_have_same_fields(
    name: str,
    element_counts: Dict[str, int]
):

    formula1 = MolecularFormula(
        name=name,
        elements={
            Element(
                name=name,
                isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in element_params[name]]
            ): count for name, count in element_counts.items()
        }
    )

    formula2 = MolecularFormula(
        name=name,
        elements={
            Element(
                name=name,
                isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in element_params[name]]
            ): count for name, count in element_counts.items()
        }
    )

    assert formula1 == formula2


@pytest.mark.parametrize('name,element_counts', formula_params)
def test__should_affirm_instance_inequality__when_molecular_formula_instances_have_different_fields(
    name: str,
    element_counts: Dict[str, int]
):

    formula1 = MolecularFormula(
        name=name,
        elements={
            Element(
                name=name,
                isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in element_params[name]]
            ): count for name, count in element_counts.items()
        }
    )

    formula2 = MolecularFormula(
        name='CH4',
        elements={
            Element(
                name=name,
                isotopes=[Isotope(name=name, mass=mass, abundance=0.5) for name, mass, abundance in element_params[name]]
            ): count for name, count in element_counts.items()
        }
    )

    assert formula1 != formula2


@pytest.mark.parametrize('name,element_counts', formula_params)
def test__should_affirm_instance_inequality__when_comparison_with_another_class(
    name: str,
    element_counts: Dict[str, int]
):

    formula = MolecularFormula(
        name=name,
        elements={
            Element(
                name=name,
                isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in element_params[name]]
            ): count for name, count in element_counts.items()
        }
    )

    assert formula != 1
    assert formula != 'str'
    assert formula != [1, 2, 3]
