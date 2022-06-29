import scipy.stats as stats


def uniform(a: float, b: float, k: float, q: float) -> float:
    """
    a: Minimaler Wert, den X annehmen kann
    b: Maximaler Wert, den X annehmen kann
    k: Ausgewählter Wert
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.uniform(loc=a, scale=b-a)
    print("----")
    print(f"Gleichverteilung-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(
        f"Gleichverteilung-Verteilungsfunktion (X ≥ {k}): {instance.sf(k)}")
    print(f"Gleichverteilung-Quantil: {instance.ppf(q)}")
    print(f"Gleichverteilung-Erwartungswert: {instance.mean()}")
    print(f"Gleichverteilung-Varianz: {instance.var()}")
    print(f"Gleichverteilung-Standardabweichung: {instance.std()}")
    print("----")


def expon(lamb: float, k: float, q: float) -> float:
    """
    lamb: Ankunftsrate der Ereignisse
    k: Ausgewählter Wert
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.expon(loc=0, scale=1/lamb)
    print("----")
    print(
        f"Exponentialverteilung-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(
        f"Exponentialverteilung-Verteilungsfunktion (X ≥ {k}): {instance.sf(k)}")
    print(f"Exponentialverteilung-Quantil: {instance.ppf(q)}")
    print(f"Exponentialverteilung-Erwartungswert: {instance.mean()}")
    print(f"Exponentialverteilung-Varianz: {instance.var()}")
    print(f"Exponentialverteilung-Standardabweichung: {instance.std()}")
    print("----")


def norm(mu: float, sig: float, k: float, q: float) -> float:
    """
    mu: Erwartungswert
    sig: Standardabweichung
    k: Ausgewählter Wert
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.norm(loc=mu, scale=sig)
    print("----")
    print(f"Normalverteilung-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(
        f"Normalverteilung-Verteilungsfunktion (X ≥ {k}): {instance.sf(k)}")
    print(f"Normalverteilung-Quantil: {instance.ppf(q)}")
    print(f"Normalverteilung-Erwartungswert: {instance.mean()}")
    print(f"Normalverteilung-Varianz: {instance.var()}")
    print(f"Normalverteilung-Standardabweichung: {instance.std()}")
    print("----")


def main():
    print()
    # Wahrscheinlichtkeit, dass Eve aus einem zufälligen Intervall zwischen 5 Sekunden und 5 Minuten
    # 1. höchstens 1 Minute zum Lesen eines Tweets benötigt (≤)
    # 2. mindestens 1 Minute zum Lesen eines Tweets benötigt (>)
    # uniform(5, 300, 60, 0.1)

    # Wahrscheinlichtkeit, dass täglich genutzte Laufschuhe, die im Mittel 18 Monate halten,
    # 1. höchstens 15 Monate halten (≤)
    # 2. mindestens 15 Monate halten (>)
    # expon(1/18, 15, 0.1)

    # Wahrscheinlichtkeit, dass ein zufällig ausgewählter Mann bei Größe ∼ N(180.3, 7.17)
    # 1. höchstens 1.75 m groß ist (≤)
    # 2. mindestens 1.75 m groß ist (>)
    # norm(180.3, 7.17, 175, 0.1)


if __name__ == "__main__":
    main()
