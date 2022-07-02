import scipy.stats as stats
import numpy as np


def bernoulli(p: float, k: int, q: float) -> float:
    """
    p: Erfolgswahrscheinlichkeit
    k: 0 | 1
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.bernoulli(p)
    print("----")
    print(f"Bernoulli-Verteilung (X = {k}): {instance.pmf(k)}")
    print(f"Bernoulli-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(f"Bernoulli-Verteilungsfunktion (X > {k}): {1 - instance.cdf(k)}")
    print(f"Bernoulli-{q*100}%-Quantil: {instance.ppf(q)}")
    print(f"Bernoulli-Erwartungswert: {instance.mean()}")
    print(f"Bernoulli-Varianz: {instance.var()}")
    print(f"Bernoulli-Standardabweichung: {instance.std()}")
    print("----")


def geom(p: float, k: int, q: float) -> float:
    """
    p: Erfolgswahrscheinlichkeit
    k: Bei welchem Versuch tritt der Erfolg ein?
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.geom(p)
    print("----")
    print(f"Geometrische-Verteilung (X = {k}): {instance.pmf(k)}")
    print(f"Geometrische-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(f"Geometrische-Verteilungsfunktion (X > {k}): {1 - instance.cdf(k)}")
    print(f"Geometrische-{q*100}%-Quantil: {instance.ppf(q)}")
    print(f"Geometrische-Erwartungswert: {instance.mean()}")
    print(f"Geometrische-Varianz: {instance.var()}")
    print(f"Geometrische-Standardabweichung: {instance.std()}")
    print("----")


def binomial(n: int, p: float, k: int, q: float) -> float:
    """
    n: Anzahl der durchgeführten Versuche
    p: Erfolgswahrscheinlichkeit
    k: Anzahl der Erfolge
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.binom(n, p)
    print("----")
    print(f"Binomial-Verteilung (X = {k}): {instance.pmf(k)}")
    print(f"Binomial-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(f"Binomial-Verteilungsfunktion (X > {k}): {1 - instance.cdf(k)}")
    print(f"Binomial-{q*100}%-Quantil: {instance.ppf(q)}")
    print(f"Binomial-Erwartungswert: {instance.mean()}")
    print(f"Binomial-Varianz: {instance.var()}")
    print(f"Binomial-Standardabweichung: {instance.std()}")
    print("----")


def hypergeom(n: int, M: int, N: int, k: int, q: float) -> float:
    """
    n: Größe der Stichprobe
    M: Anzahl der Elemente mit der gewünschten Eigenschaft
    N: Anzahl aller Elemente
    k: Gesuchte Anzahl der Elemente mit der gewünschten Eigenschaft
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.hypergeom(M=N, n=M, N=n)
    print("----")
    print(f"Hypergeometrische-Verteilung (X = {k}): {instance.pmf(k)}")
    print(
        f"Hypergeometrische-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(
        f"Hypergeometrische-Verteilungsfunktion (X > {k}): {1 - instance.cdf(k)}")
    print(f"Hypergeometrische-{q*100}%-Quantil: {instance.ppf(q)}")
    print(f"Hypergeometrische-Erwartungswert: {instance.mean()}")
    print(f"Hypergeometrische-Varianz: {instance.var()}")
    print(f"Hypergeometrische-Standardabweichung: {instance.std()}")
    print("----")


def poisson(p: float, k: int, q: float) -> float:
    """
    p: (Durchschnittliche) Auftrittsrate
    k: Gesuchte Auftrittsrate
    q: Quantil-Wert (z.B. 0.75)
    """
    instance = stats.poisson(p)
    print("----")
    print(f"Poisson-Verteilung (X = {k}): {instance.pmf(k)}")
    print(f"Poisson-Verteilungsfunktion (X ≤ {k}): {instance.cdf(k)}")
    print(f"Poisson-Verteilungsfunktion (X > {k}): {1 - instance.cdf(k)}")
    print(f"Poisson-{q*100}%-Quantil: {instance.ppf(q)}")
    print(f"Poisson-Erwartungswert: {instance.mean()}")
    print(f"Poisson-Varianz: {instance.var()}")
    print(f"Poisson-Standardabweichung: {instance.std()}")
    print("----")


def main():
    print()
    # Wurf einer Münze mit 50% Erfolgswahrscheinlichkeit auf Seite 1 (z.B. Kopf)
    # bernoulli(0.5, 1, 0.1)

    # Wahrscheinlichtkeit, dass eine Snowboarderin bei einer Erfolgwahrscheinlichkeit von 40%
    # 1. im 2ten Versuche eine erfolgreiche Abfahrt absolviert (=)
    # 2. höchstens 2 Versuche bis zur ersten Abfahrt braucht (≤)
    # 3. mehr als 2 Versuche bis zur ersten Abfahrt braucht (>)
    # geom(0.4, 2, 0.1)

    # Wahrscheinlichkeit, dass Britta bei einer Erfolgwahrscheinlichkeit von 25% von 5 Schneebällen
    # 1. genau 2 mal trifft
    # 2. höchstens 2 mal trifft
    # 3. mehr als 2 mal trifft
    # binomial(11, 0.55, 8, 0.1)

    # Wahrscheinlichkeit, dass bei einem 10-köpfigen Orga-Team aus einer Gruppe von 70 Studierenden, von denen 45 aus der Fakultät IN kommen,
    # 1. genau 10-IN Studierende mitorganisieren
    # 2. höchstens 10-IN Studierende mitorganisieren
    # 3. mehr als 10-IN Studierende mitorganisieren
    # hypergeom(10, 45, 70, 10, 0.1)

    # Wahrscheinlichkeit, dass eine Maschine mit ca. 3 Ausfällen pro Woche
    # 1. diese Woche 2 mal ausfällt
    # 2. diese Woche höchstens 2 mal ausfällt
    # 3. diese Woche mindestens 2 mal ausfällt
    # poisson(3, 2, 0.1)


if __name__ == "__main__":
    main()
