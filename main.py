from time import sleep

from fire import Fire

from src import lib
from src.contingency_table import ContingencyTable


class CLI:
    def visualize(self, x11, x12, x21, x22, sample=10):
        current = ContingencyTable([x11, x12, x21, x22])
        for idx in range(sample):
            print(idx + 1)
            print(current)
            print("\n")
            current = current.next()
            sleep(1)

    def dist(self, x11, x12, x21, x22, burn_in=0, sample=1000):
        observed = ContingencyTable([x11, x12, x21, x22])
        cts = []
        current = observed
        for _ in range(burn_in):
            current = current.next()
        for _ in range(sample):
            current = current.next()
            cts.append(current)
        tallied = lib.dist(cts)
        tallied = sorted(tallied.items(), key=lambda t: t[0].frequencies[0])
        for ct, prob in tallied:
            print(ct, prob)

    def p_value(self, x11, x12, x21, x22, burn_in=0, sample=1000):
        observed = ContingencyTable([x11, x12, x21, x22])
        cts = []
        current = observed
        for _ in range(burn_in):
            current = current.next()
        for _ in range(sample):
            current = current.next()
            cts.append(current)
        print(lib.p_value(observed, cts))


if __name__ == "__main__":
    Fire(CLI)
