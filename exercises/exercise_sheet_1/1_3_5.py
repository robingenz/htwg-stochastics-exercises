import numpy as np
from scipy.stats import iqr


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


def main():
    values = [1, 1, 1, 2, 3, 3, 3, 4, 5, 5]
    print(f"Arithmetisches Mittel: {mean(values)}")
    print(f"Median: {median(values)}")
    print(f"Modalwert: {mode(values)}")
    print(f"25%-Quantil: {quantile(values, 0.25)}")
    print(f"30%-Quantil: {quantile(values, 0.3)}")
    print(f"66%-Quantil: {quantile(values, 0.66)}")
    print(f"Varianz: {variance(values)}")
    print(f"Standardabweichung: {standard_deviation(values)}")
    print(f"Interquartilabstand: {interquartile_range(values)}")
    print(f"Spannweite: {span(values)}")


if __name__ == "__main__":
    main()
