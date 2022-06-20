import numpy as np
from scipy.stats import iqr
from statistics import covariance as cov


def mean(values: list) -> float:
    return np.mean(values)


def median(values: list) -> float:
    return np.median(values)


def mode(values: list) -> float:
    return max(set(values), key=values.count)


def quantile(values: list, q: float) -> float:
    return np.quantile(values, q, method="averaged_inverted_cdf")


def variance(values: list) -> float:
    return np.var(values, ddof=1)


def standard_deviation(values: list) -> float:
    return np.std(values, ddof=1)


def interquartile_range(values: list) -> float:
    return iqr(values, interpolation="averaged_inverted_cdf")


def span(values: list) -> float:
    max_value = max(values)
    min_value = min(values)
    return max_value - min_value


def covariance(values1: list, values2: list) -> float:
    return cov(values1, values2)


def correlation_coefficient(values1: list, values2: list) -> float:
    return covariance(values1, values2) / (standard_deviation(values1) * standard_deviation(values2))


def main():
    values1 = [1, 2, 3, 4]
    values2 = [1, 2, 3, 4]
    print(f"Arithmetisches Mittel: {mean(values1)}")
    print(f"Median: {median(values1)}")
    print(f"Modalwert: {mode(values1)}")
    print(f"25%-Quantil: {quantile(values1, 0.25)}")
    print(f"30%-Quantil: {quantile(values1, 0.3)}")
    print(f"66%-Quantil: {quantile(values1, 0.66)}")
    print(f"Varianz: {variance(values1)}")
    print(f"Standardabweichung: {standard_deviation(values1)}")
    print(f"Interquartilabstand: {interquartile_range(values1)}")
    print(f"Spannweite: {span(values1)}")
    print(
        f"Kovarianz: {covariance(values1, values2)}")
    print(
        f"Korrelationskoeffizient: {correlation_coefficient(values1, values2)}")


if __name__ == "__main__":
    main()
