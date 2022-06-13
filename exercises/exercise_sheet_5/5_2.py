from scipy.stats import binom


def binomial(n: int, p: float, k: int) -> float:
    return binom.pmf(k=k, n=n, p=p)


def main():
    n = 31
    p = 0.258
    print(f"x = 0: {format(binomial(n, p, 0),'.4f')}")
    print(f"x = 1: {format(binomial(n, p, 1),'.4f')}")
    print(f"x = 2: {format(binomial(n, p, 2),'.4f')}")
    print(f"x = 3: {format(binomial(n, p, 3),'.4f')}")


if __name__ == "__main__":
    main()
