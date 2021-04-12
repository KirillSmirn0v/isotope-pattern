import pytest

from isotope_pattern_lib.types.types import Isotope


isotope_params = [
    ('C12', 12.0, 0.989),
    ('O16', 15.9949146, 0.998),
    ('N15', 15.0001089, 0.004)
]


@pytest.mark.parametrize('name,mass,abundance', isotope_params)
def test__should_affirm_instance_equality__when_isotope_instances_have_same_fields(
    name: str,
    mass: float,
    abundance: float
):

    isotope1 = Isotope(name=name, mass=mass, abundance=abundance)
    isotope2 = Isotope(name=name, mass=mass, abundance=abundance)

    assert isotope1 == isotope2
    assert hash(isotope1) == hash(isotope2)


@pytest.mark.parametrize('name,mass,abundance', isotope_params)
def test__should_affirm_instance_inequality__when_isotope_instances_have_different_fields(
    name: str,
    mass: float,
    abundance: float
):

    isotope1 = Isotope(name=name, mass=mass, abundance=abundance)
    isotope2 = Isotope(name='C12', mass=15.9949146, abundance=0.004)

    assert isotope1 != isotope2
    assert hash(isotope1) != hash(isotope2)
