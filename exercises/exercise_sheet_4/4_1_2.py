import numpy as np


def expected_value(values: list) -> int:
    unique, counts = np.unique(np.asarray(values), return_counts=True)
    weights = np.asarray(list(map(lambda count: count / len(values), counts)))
    return (unique * weights).sum() / weights.sum()


def variance(values: list) -> int:
    return np.var(values)


def standard_deviation(values: list) -> int:
    return np.std(values)


def main():
    values = [1, 1, 1, 1, 2, 3, 3, 3, ]
    print(f"Erwartungswert: {expected_value(values)}")
    print(f"Varianz: {variance(values)}")
    print(f"Standardabweichung: {standard_deviation(values)}")


if __name__ == "__main__":
    main()
