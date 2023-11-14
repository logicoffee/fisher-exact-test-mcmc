from src.contingency_table import ContingencyTable


def p_value(observed: ContingencyTable, cts: list[ContingencyTable]) -> float:
    index = observed.min_index
    observed_value = observed.frequencies[index]
    values = [ct.frequencies[index] for ct in cts]
    filtered = [v for v in values if v <= observed_value]
    return len(filtered) / len(values)
