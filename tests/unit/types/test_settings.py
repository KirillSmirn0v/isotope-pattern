from os import path

import pytest

from isotope_pattern_lib.types.settings import Settings
from isotope_pattern_lib.types.types import (
    Element,
    Isotope
)


@pytest.mark.parametrize('file_path', ['config_good.yaml', 'config_good.json'])
def test__should_parse_elements__when_config_file_is_correct(file_path: str):

    full_path = path.join('tests', 'data', 'unit', file_path)

    settings = Settings.parse_from_file(full_path)
    elements = settings.elements

    assert len(elements) == 3

    assert Element(
        name='H',
        isotopes=[Isotope(name='H1', mass=1.0078250, abundance=1.00)]
    ) in elements
    assert Element(
        name='C',
        isotopes=[
            Isotope(name='C12', mass=12.0, abundance=0.989),
            Isotope(name='C13', mass=13.0033548, abundance=0.011)
        ]
    ) in elements
    assert Element(
        name='O',
        isotopes=[
            Isotope(name='O16', mass=15.9949146, abundance=0.998),
            Isotope(name='O18', mass=17.9991596, abundance=0.002)
        ]
    ) in elements


@pytest.mark.parametrize(
    'file_path,error',
    [
        ('no_file.yaml', FileNotFoundError),
        ('config_missing_fields.yaml', KeyError),
        ('config_invalid_fields.yaml', KeyError)
    ]
)
def test__should_raise_error__when_config_file_is_corrupted_or_absent(
    file_path: str,
    error: Exception
):

    full_path = path.join('tests', 'data', 'unit', file_path)

    with pytest.raises(expected_exception=error):
        Settings.parse_from_file(path=full_path)
