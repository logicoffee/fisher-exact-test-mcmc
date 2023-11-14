from math import log10

from numpy import argmin, random
from scipy.stats import hypergeom


class ContingencyTable:
    frequencies: list[int]
    min_index: int

    template = """
┏━━━━━┳━━━━━┓
┃ {f0} ┃ {f1} ┃
┣━━━━━╋━━━━━┫
┃ {f2} ┃ {f3} ┃
┗━━━━━┻━━━━━┛
    """

    def __init__(self, frequencies: list[int]):
        self.frequencies = frequencies
        self.min_index = argmin(self.frequencies)

    def __str__(self):
        return self.template.format(
            f0=int_to_str(self.frequencies[0]),
            f1=int_to_str(self.frequencies[1]),
            f2=int_to_str(self.frequencies[2]),
            f3=int_to_str(self.frequencies[3]),
        )

    def hypergeom_pmf(self) -> float:
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html
        # TODO: 本来は超幾何分布の確率を計算する必要はない
        type1 = self.frequencies[0] + self.frequencies[1]
        type2 = self.frequencies[2] + self.frequencies[3]
        total = type1 + type2
        drawn = self.frequencies[0] + self.frequencies[2]
        return hypergeom.pmf(self.frequencies[0], total, type1, drawn)

    def _validate(self) -> bool:
        return min(self.frequencies) >= 0

    def _accept(self, candidate) -> bool:
        u = random.rand()
        ratio = candidate.hypergeom_pmf() / self.hypergeom_pmf()
        return u <= ratio

    def _get_candidate(self):
        if random.rand() >= 0.5:
            epsilon = 1
        else:
            epsilon = -1

        return ContingencyTable(
            [
                self.frequencies[0] + epsilon,
                self.frequencies[1] - epsilon,
                self.frequencies[2] - epsilon,
                self.frequencies[3] + epsilon,
            ]
        )

    def next(self):
        cand = self._get_candidate()
        if not cand._validate():
            return self
        if self._accept(cand):
            return cand
        return self


def int_to_str(i: int, length: int = 3):
    if i == 0:
        digits = 1
    else:
        digits = int(log10(i)) + 1
    return ' ' * (length - digits) + str(i)
