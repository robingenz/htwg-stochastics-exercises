import numpy as np
from statistics import covariance as cov


def mean(values: list) -> float:
    return np.mean(values)


def standard_deviation(values: list) -> float:
    return np.std(values, ddof=1)


def covariance(values1: list, values2: list) -> float:
    return cov(values1, values2)


def correlation_coefficient(values1: list, values2: list) -> float:
    return covariance(values1, values2) / (standard_deviation(values1) * standard_deviation(values2))


def main():
    x1 = [28300, 28000, 41000, 40000, 48000, 47500,
          43000, 50700, 50000, 48000, 25000, 24000]
    x2 = [1.6, 2.6, 3.7, 5.3, 6.9, 7.1, 7.2, 6.7, 5.1, 3.6, 2.1, 1.4]
    print(f"Korrelationskoeffizient: {correlation_coefficient(x1, x2)}")


if __name__ == "__main__":
    main()
