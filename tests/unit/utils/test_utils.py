from typing import (
    Set,
    Tuple
)

import pytest

from isotope_pattern_lib.utils import utils


@pytest.mark.parametrize(
    'total_sum,size,expected_result',
    [
        (0, 1, {(0,)}),
        (10, 1, {(10,)}),
        (1, 2, {(1, 0), (0, 1)}),
        (1, 3, {(1, 0, 0), (0, 1, 0), (0, 0, 1)}),
        (2, 3, {(2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 1, 0), (1, 0, 1), (0, 1, 1)}),
        (5, 2, {(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)})
    ]

)
def test__should_return_correct_array__when_generate_arrays_with_preserved_sum_is_called(
    total_sum: int,
    size: int,
    expected_result: Set[Tuple]
):

    actual_result = list(utils.generate_arrays_with_preserved_sum(total_sum=total_sum, size=size))
    actual_result = set([tuple(item) for item in actual_result])

    assert len(actual_result.intersection(expected_result)) == len(expected_result)
    assert len(expected_result.intersection(actual_result)) == len(expected_result)
