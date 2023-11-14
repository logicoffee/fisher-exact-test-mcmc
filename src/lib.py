from src.contingency_table import ContingencyTable


def p_value(cts: list[ContingencyTable]) -> float:
    obs = cts[0]
    index = obs.min_index
    values = [ct.frequencies[index] for ct in cts]
    filtered = [v for v in values if v <= values[0]]
    return len(filtered) / len(values)
