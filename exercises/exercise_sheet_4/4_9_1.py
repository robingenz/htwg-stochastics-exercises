import numpy as np
from statistics import covariance as cov


def expected_value(values: list) -> float:
    return np.average(values)


def variance(values: list) -> float:
    return np.var(values)


def covariance(values1: list, values2: list) -> float:
    return cov(values1, values2)


def main():
    x1 = [1] * 5 + [2] * 5 + [3] * 5 + [4] * 5 + [5] * 5
    x2 = [1] * 5 + [2] * 5 + [3] * 5 + [4] * 5 + [5] * 5
    x3 = [-4] * 1 + [-3] * 2 + [-2] * 3 + [-1] * 4 + \
        [0] * 5 + [1] * 4 + [2] * 3 + [3] * 2 + [4] * 1
    x4 = [2] * 1 + [3] * 2 + [4] * 3 + [5] * 4 + [6] * \
        5 + [7] * 4 + [8] * 3 + [9] * 2 + [10] * 1
    print("---- x1 ----")
    print(f"Erwartungswert: {expected_value(x1)}")
    print(f"Varianz: {variance(x1)}")
    print("---- x2 ----")
    print(f"Erwartungswert: {expected_value(x2)}")
    print(f"Varianz: {variance(x2)}")
    print("---- x3 ----")
    print(f"Erwartungswert: {expected_value(x3)}")
    print(f"Varianz: {variance(x3)}")
    print("---- x4 ----")
    print(f"Erwartungswert: {expected_value(x4)}")
    print(f"Varianz: {variance(x4)}")
    print("---- x1 + x2 ----")
    print(f"Kovarianz: {covariance(x1, x2)}")
    print("---- x1 + x3 ----")
    print(f"Kovarianz: {covariance(x1, x3)}")
    print("---- x2 + x3 ----")
    print(f"Kovarianz: {covariance(x2, x3)}")


if __name__ == "__main__":
    main()
