import numpy as np
from scipy.stats import iqr


def mean(values: list) -> int:
    return np.mean(values)


def median(values: list) -> int:
    return np.median(values)


def quantile(values: list, q: float) -> int:
    return np.quantile(values, q)


def standard_deviation(values: list) -> int:
    return np.std(values)


def main():
    values = [25, 10, 30, 25, 35, 25]
    print(f"Arithmetisches Mittel: {mean(values)}")
    print(f"Median: {median(values)}")
    print(f"75%-Quantil: {quantile(values, 0.75)}")
    print(f"Standardabweichung: {standard_deviation(values)}")


if __name__ == "__main__":
    main()
