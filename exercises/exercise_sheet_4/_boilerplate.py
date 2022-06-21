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
    values1 = [1] * 5 + [1, 2, 3, 4]
    values2 = [1] * 5 + [1, 2, 3, 4]
    print(f"Erwartungswert: {expected_value(values1)}")
    print(f"Varianz: {variance(values1)}")
    print(f"Standardabweichung: {standard_deviation(values1)}")
    print(f"Kovarianz: {covariance(values1, values2)}")
    print(
        f"Korrelationskoeffizient: {correlation_coefficient(values1, values2)}")


if __name__ == "__main__":
    main()
