from typing import (
    List,
    Tuple
)

import pytest

from isotope_pattern_lib.types.types import (
    Element,
    Isotope
)


element_params = [
    ('C', [('C12', 12.0, 0.989), ('C13', 13.0033548, 0.011)]),
    ('H', [('H1', 1.0078250, 1.000)]),
    ('O', [('O16', 15.9949146, 0.998), ('O18', 17.9991596, 0.002)])
]


@pytest.mark.parametrize('name,isotopes', element_params)
def test__should_affirm_instance_equality__when_element_instances_have_same_fields(
    name: str,
    isotopes: List[Tuple[str, float, float]]
):

    element1 = Element(
        name=name,
        isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in isotopes]
    )
    element2 = Element(
        name=name,
        isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in isotopes]
    )

    assert element1 == element2
    assert hash(element1) == hash(element2)


@pytest.mark.parametrize('name,isotopes', element_params)
def test__should_affirm_instance_inequality__when_element_instances_have_different_fields(
    name: str,
    isotopes: List[Tuple[str, float, float]]
):

    element1 = Element(
        name=name,
        isotopes=[Isotope(name=name, mass=mass, abundance=abundance) for name, mass, abundance in isotopes]
    )
    element2 = Element(
        name='H',
        isotopes=[Isotope(name='H1', mass=1.0078250, abundance=0.5)]
    )

    assert element1 != element2
    assert hash(element1) != hash(element2)
