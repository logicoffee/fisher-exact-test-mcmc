from math import log10

from numpy import random


class ContingencyTable:
    frequencies: list[int]

    template = """\
┏━━━━━┳━━━━━┓
┃ {f0} ┃ {f1} ┃
┣━━━━━╋━━━━━┫
┃ {f2} ┃ {f3} ┃
┗━━━━━┻━━━━━┛"""

    def __init__(self, frequencies: list[int]):
        self.frequencies = frequencies

    def __str__(self):
        return self.template.format(
            f0=int_to_str(self.frequencies[0]),
            f1=int_to_str(self.frequencies[1]),
            f2=int_to_str(self.frequencies[2]),
            f3=int_to_str(self.frequencies[3]),
        )

    def next(self):
        cand = self._get_candidate()
        if not cand._validate():
            return self
        if self._accept(cand):
            return cand
        return self

    def create_new(self, index, value):
        diff = value - self.frequencies[index]
        epsilon = 1 if index in [0, 3] else -1
        return ContingencyTable(
            [
                self.frequencies[0] + epsilon * diff,
                self.frequencies[1] - epsilon * diff,
                self.frequencies[2] - epsilon * diff,
                self.frequencies[3] + epsilon * diff,
            ]
        )

    def _validate(self) -> bool:
        return min(self.frequencies) >= 0

    def _accept(self, candidate) -> bool:
        u = random.rand()
        ratio = 1
        for num, denom in zip(self.frequencies, candidate.frequencies):
            if num == denom:
                continue
            elif num < denom:
                ratio /= denom
            elif num > denom:
                ratio *= num
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


def int_to_str(i: int, length: int = 3):
    if i == 0:
        digits = 1
    else:
        digits = int(log10(i)) + 1
    return ' ' * (length - digits) + str(i)
