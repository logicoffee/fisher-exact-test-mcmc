from functools import reduce

from numpy import argmin

from src.contingency_table import ContingencyTable


def p_value(observed: ContingencyTable, cts: list[ContingencyTable]) -> float:
    index = argmin(observed.frequencies)
    observed_value = observed.frequencies[index]
    values = [ct.frequencies[index] for ct in cts]
    filtered = [v for v in values if v <= observed_value]
    return len(filtered) / len(values)


def dist(cts: list[ContingencyTable]) -> dict[ContingencyTable, float]:
    values = [ct.frequencies[0] for ct in cts]

    def reducer(acc: dict[int, int], cur: int) -> dict[int, int]:
        if cur in acc:
            acc[cur] += 1
        else:
            acc[cur] = 1
        return acc

    tallied = reduce(reducer, values, {})
    tallied = {key: value / len(values) for key, value in tallied.items()}
    some = cts[0]
    return {some.create_new(0, key): value for key, value in tallied.items()}
