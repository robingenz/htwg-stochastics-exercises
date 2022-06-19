import numpy as np


def median(values: list) -> float:
    return np.median(values)


def main():
    values = [5, 10, 20, 50, 100, 200, 500]
    print(f"Median: {median(values)}")
    values = [5, 10, 20, 50, 100, 200, 500, 1000]
    print(f"Median (mit 1000€-Schein): {median(values)}")


if __name__ == "__main__":
    main()
