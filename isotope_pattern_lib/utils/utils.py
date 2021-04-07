from typing import List


def generate_arrays_with_preserved_sum(total_sum: int, size: int) -> List[List[int]]:
    if size == 1:
        yield [total_sum]
    else:
        for i in range(total_sum + 1):
            for j in generate_arrays_with_preserved_sum(total_sum=total_sum - i, size=size - 1):
                yield [i] + j