from scipy.stats import binom
import numpy as np


def expected_value(values: list) -> int:
    return np.average(values)


def binomial(n: int, p: float, k: int) -> float:
    return binom.pmf(k=k, n=n, p=p)


def main():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Erwartungswert: {expected_value(values)}")
    print("---- Wahrscheinlichkeitsverteilung ----")
    n = 5
    p = 0.1
    print(f"x = 0: {format(binomial(n, p, 0),'.4f')}")
    print(f"x = 1: {format(binomial(n, p, 1),'.4f')}")
    print(f"x = 2: {format(binomial(n, p, 2),'.4f')}")
    print(f"x = 3: {format(binomial(n, p, 3),'.4f')}")
    print(f"x = 4: {format(binomial(n, p, 4),'.4f')}")
    print(f"x = 5: {format(binomial(n, p, 5),'.4f')}")


if __name__ == "__main__":
    main()
