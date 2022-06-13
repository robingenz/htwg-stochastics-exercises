import scipy.stats as stats


def poisson(mu: int, k: int) -> float:
    return stats.poisson.pmf(k=k, mu=mu)


def poisson_sum(mu: int, k: int) -> float:
    return stats.poisson.cdf(k=k, mu=mu)


def main():
    mu = 5
    print(f"a) {format(poisson(mu, 3), '.4f')}")
    print(f"b) {format(1-poisson_sum(mu, 4), '.4f')}")


if __name__ == "__main__":
    main()
