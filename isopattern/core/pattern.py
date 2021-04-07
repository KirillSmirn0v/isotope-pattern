import itertools
from typing import (
    List,
    FrozenSet,
)

from scipy.stats import multinomial

from isopattern.core.types import (
    Isotope,
    IsotopeFormula,
    MolecularFormula,
)


def compute(formula: MolecularFormula) -> List[IsotopeFormula]:

    element_isotope_formulas = {}
    for element, count in formula.elements.items():
        element_isotope_formulas[element] = compute_isotope_distributions(element.isotopes, count)

    for combination in itertools.product(*element_isotope_formulas.values()):

        name = ""
        counts = {}
        probability = 1.0
        for isotope_formula in combination:
            name += isotope_formula.name
            counts.update(isotope_formula.isotopes)
            probability *= isotope_formula.probability

        yield IsotopeFormula(
            name=name,
            isotopes=counts,
            probability=probability,
        )


def compute_isotope_distributions(isotopes: FrozenSet[Isotope], element_count: int) -> List[IsotopeFormula]:

    isotope_list = list(isotopes)
    distribution = multinomial(n=element_count, p=[isotope.abundance for isotope in isotope_list])

    isotope_formulas = []
    for array in generate_arrays_with_preserved_sum(total_sum=element_count, size=len(isotope_list)):
        probability = distribution.pmf(array)
        isotope_counts = dict(zip(isotope_list, array))
        isotope_formulas.append(IsotopeFormula(
            name="".join([f"{isotope.name}[{count}]" for isotope, count in isotope_counts.items()]),
            isotopes=isotope_counts,
            probability=probability
        ))

    return isotope_formulas


def generate_arrays_with_preserved_sum(total_sum: int, size: int) -> List[List[int]]:
    if size == 1:
        yield [total_sum]
    else:
        for i in range(total_sum + 1):
            for j in generate_arrays_with_preserved_sum(total_sum=total_sum - i, size=size - 1):
                yield [i] + j
