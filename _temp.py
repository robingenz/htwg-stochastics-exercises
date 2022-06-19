import numpy as np
from statistics import covariance as cov


def mean(values: list) -> float:
    return np.mean(values)


def standard_deviation(values: list) -> float:
    return np.std(values)


def covariance(values1: list, values2: list) -> float:
    return cov(values1, values2)


def correlation_coefficient(values1: list, values2: list) -> int:
    print(mean(values1))
    print(mean(values2))
    return covariance(values1, values2) / (standard_deviation(values1) * standard_deviation(values2))


def main():
    x1 = [40, 10, 20, 30, 50, 60]
    x2 = [2, 7, 3, 5, 1, 3]
    print(f"Korrelationskoeffizient: {correlation_coefficient(x1, x2)}")


if __name__ == "__main__":
    main()
