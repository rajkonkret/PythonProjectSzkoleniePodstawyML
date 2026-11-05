import duckdb
import pandas as pd

df = pd.DataFrame(
    {
        "sklep": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],

        "miesiac": ["styczeń", "luty", "marzec", "styczeń", "luty", "marzec", "styczeń", "luty", "marzec"],

        "sprzedaz": [1200, 1500, 1700, 900, 1100, 1300, 2000, 1900, 2200]
    }
)

# pokaz wszystkie wyniki dane
wynik1 = duckdb.sql(
    """SELECT * FROM df"""
)

print(wynik1)

wynik2 = duckdb.sql(
    """SELECT *
    FROM df
    WHERE sprzedaz > 1500
    """
)

print(wynik2)
# ┌─────────┬─────────┬──────────┐
# │  sklep  │ miesiac │ sprzedaz │
# │ varchar │ varchar │  int64   │
# ├─────────┼─────────┼──────────┤
# │ A       │ marzec  │     1700 │
# │ C       │ styczeń │     2000 │
# │ C       │ luty    │     1900 │
# │ C       │ marzec  │     2200 │
# └─────────┴─────────┴──────────┘

wynik2 = duckdb.sql(
    """SELECT *
    FROM df
    WHERE sprzedaz > 1500
    """
).df()

print(wynik2)
#   sklep  miesiac  sprzedaz
# 0     A   marzec      1700
# 1     C  styczeń      2000
# 2     C     luty      1900
# 3     C   marzec      2200

wynik3 = duckdb.sql("""

    SELECT

        sklep,

        SUM(sprzedaz) AS suma_sprzedazy

    FROM df

    GROUP BY sklep

    ORDER BY suma_sprzedazy DESC

""").df()

print("\nSuma sprzedaży dla każdego sklepu:")

print(wynik3)
# Suma sprzedaży dla każdego sklepu:
#   sklep  suma_sprzedazy
# 0     C          6100.0
# 1     A          4400.0
# 2     B          3300.0
