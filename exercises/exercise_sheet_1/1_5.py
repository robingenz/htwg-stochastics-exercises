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


def interquartile_range(values: list) -> float:
    return iqr(values, interpolation="averaged_inverted_cdf")


def span(values: list) -> float:
    max_value = max(values)
    min_value = min(values)
    return max_value - min_value


def main():
    values = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]
    print(f"Arithmetisches Mittel: {mean(values)}")
    print(f"Median: {median(values)}")
    print(f"Modalwert: {mode(values)}")
    print(f"10%-Quantil: {quantile(values, 0.10)}")
    print(f"25%-Quantil: {quantile(values, 0.25)}")
    print(f"75%-Quantil: {quantile(values, 0.75)}")
    print(f"Interquartilabstand: {interquartile_range(values)}")
    print(f"Spannweite: {span(values)}")


if __name__ == "__main__":
    main()
