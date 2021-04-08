import copy
from typing import Dict

import pytest
from _pytest.fixtures import SubRequest

from isotope_pattern_lib.types.settings import Settings
from isotope_pattern_lib.types.types import (
    Element,
    Isotope
)


@pytest.fixture
def settings(request: SubRequest) -> Settings:

    file_path = request.param['file_path']

    return Settings.parse_from_file(path=file_path)


@pytest.fixture
def isotope_map() -> Dict[str, Isotope]:

    return copy.deepcopy({
        'C12': Isotope(name='C12', mass=12.0000000, abundance=0.989),
        'C13': Isotope(name='C13', mass=13.0033548, abundance=0.011),
        'H1': Isotope(name='H1', mass=1.0078250, abundance=1.000),
        'O16': Isotope(name='O16', mass=15.9949146, abundance=0.998),
        'O18': Isotope(name='O18', mass=17.9991596, abundance=0.002)
    })


@pytest.fixture
def element_map(isotope_map: Dict[str, Isotope]) -> Dict[str, Element]:

    return copy.deepcopy({
        'C': Element(name='C', isotopes=frozenset([isotope_map['C12'], isotope_map['C13']])),
        'H': Element(name='H', isotopes=frozenset([isotope_map['H1']])),
        'O': Element(name='O', isotopes=frozenset([isotope_map['O16'], isotope_map['O18']]))
    })
