import numpy as np


def expected_value(values: list) -> float:
    return np.average(values)


def variance(values: list) -> float:
    return np.var(values)


def standard_deviation(values: list) -> float:
    return np.std(values)


def main():
    # values = [1] * 4 + [2] + [3] * 3
    values = [1, 1, 1, 1, 2, 3, 3, 3]
    print(f"Erwartungswert: {expected_value(values)}")
    print(f"Varianz: {variance(values)}")
    print(f"Standardabweichung: {standard_deviation(values)}")


if __name__ == "__main__":
    main()
