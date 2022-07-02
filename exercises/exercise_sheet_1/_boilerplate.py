import numpy as np
from scipy.stats import iqr
from statistics import covariance as cov


def occurrences(values: list) -> dict:
    return dict((x, values.count(x)) for x in set(values))


def mean(values: list) -> float:
    return np.mean(values)


def median(values: list) -> float:
    return np.median(values)


def mode(values: list) -> list:
    maxCount = values.count(max(set(values), key=values.count))
    return set([value for value in values if values.count(value) == maxCount])


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
    values1 = [1.3, 5, 1.3, 2.7, 4, 3.7]
    values2 = [2, 3, 1, 2, 1, 2.7]
    print(f"Absolute Häufigkeit: {occurrences(values1)}")
    print(f"Arithmetisches Mittel (x̄): {mean(values1)}")
    print(f"Median (˜x): {median(values1)}")
    print(f"Modalwert (x_m): {mode(values1)}")
    q1 = 0.25
    print(f"{q1*100}%-Quantil (˜x_{q1}): {quantile(values1, q1)}")
    q2 = 0.5
    print(f"{q2*100}%-Quantil (˜x_{q2}): {quantile(values1, q2)}")
    q3 = 0.75
    print(f"{q3*100}%-Quantil (˜x_{q3}): {quantile(values1, q3)}")
    print(f"Varianz (s^2): {variance(values1)}")
    print(f"Standardabweichung (s): {standard_deviation(values1)}")
    print(f"Interquartilabstand (I): {interquartile_range(values1)}")
    print(f"Spannweite (R): {span(values1)}")
    print(
        f"Kovarianz (s_x,y): {covariance(values1, values2)}")
    print(
        f"Korrelationskoeffizient (r_x,y): {correlation_coefficient(values1, values2)}")


if __name__ == "__main__":
    main()
