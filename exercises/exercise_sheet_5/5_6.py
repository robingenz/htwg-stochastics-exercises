import scipy.stats as stats


def binom(n: int, p: float, k: int) -> float:
    return stats.binom.cdf(k=k, n=n, p=p)


def poisson(mu: int, k: int) -> float:
    return stats.poisson.pmf(k=k, mu=mu)


def geom(p: float, k: int) -> float:
    return 1 - (1 - p)**k


# See https://towardsdatascience.com/bernoulli-distribution-with-python-from-scratch-89fda3c822b
# def bernoulli(p: float, x: int) -> float:
#     return p**x*(1-p)**(1-x)


# See https://gist.github.com/fbrundu/cfa675c1d79b4ade4724
def hypergeom(n: int, M: int, N: int, k: int) -> float:
    return stats.hypergeom.pmf(k=k, M=N, n=M, N=n)


def main():
    n = 10
    p = 0.3
    print(f"a) {format(binom(n, p, 2), '.4f')}")
    print(f"b) {format(poisson(1, 0), '.4f')}")
    print(f"c) {format(geom(0.2, 3), '.4f')}")
    print(f"d) {format(hypergeom(3, 10, 60, 0), '.4f')}")


if __name__ == "__main__":
    main()
