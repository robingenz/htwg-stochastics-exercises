import scipy.stats as stats


def poisson(mu: int, k: int) -> float:
    return stats.poisson.cdf(k=k, mu=mu)


def main():
    mu = 9
    print(format(poisson(mu, 5), '.4f'))


if __name__ == "__main__":
    main()
