import scipy.stats as stats


def binom(n: int, p: float, k: int) -> float:
    return stats.binom.cdf(k=k, n=n, p=p)


def geom(p: float, k: int) -> float:
    return 1 - (1 - p)**k


def main():
    n = 50
    p = 0.1
    print(format(binom(n, p, 2), '.4f'))
    print(format(geom(p, 5), '.4f'))


if __name__ == "__main__":
    main()
