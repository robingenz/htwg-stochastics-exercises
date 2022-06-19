import numpy as np
from statistics import covariance as cov


def expected_value(values: list) -> float:
    return np.average(values)


def variance(values: list) -> float:
    return np.var(values)


def standard_deviation(values: list) -> float:
    return np.std(values)


def covariance(values1: list, values2: list) -> float:
    return cov(values1, values2)


def correlation_coefficient(values1: list, values2: list) -> float:
    return covariance(values1, values2) / (standard_deviation(values1) * standard_deviation(values2))


def main():
    x1 = [1, 2, 3]
    x2 = [1, 2, 3]
    x3 = [2, 3, 3, 4, 4, 4, 5, 5, 6]
    print("---- x1 ----")
    print(f"Erwartungswert: {expected_value(x1)}")
    print(f"Varianz: {variance(x1)}")
    print(f"Standardabweichung: {standard_deviation(x1)}")
    print(f"Standardabweichung: {standard_deviation(x2)}")
    print("---- x1 + x2 ----")
    print(f"Kovarianz: {covariance(x1, x2)}")
    print(f"Korrelationskoeffizient: {correlation_coefficient(x1, x2)}")
    print("---- x3 ----")
    print(f"Erwartungswert: {expected_value(x3)}")
    print(f"Varianz: {variance(x3)}")


if __name__ == "__main__":
    main()
