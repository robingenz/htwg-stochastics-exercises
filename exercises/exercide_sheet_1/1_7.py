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
    values = [250, 330, 250, 350, 270, 300, 260, 330, 200, 400]
    print(f"Arithmetisches Mittel: {mean(values)}")
    print(f"Median: {median(values)}")
    print(f"90%-Quantil: {quantile(values, 0.90)}")
    print(f"Standardabweichung: {standard_deviation(values)}")


if __name__ == "__main__":
    main()
