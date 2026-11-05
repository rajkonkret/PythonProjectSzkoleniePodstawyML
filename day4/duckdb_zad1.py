import duckdb
import pandas as pd

df = pd.DataFrame(
    {
     "sklep": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],

    "miesiac": ["styczeń", "luty", "marzec", "styczeń", "luty", "marzec", "styczeń", "luty", "marzec"],

    "sprzedaz": [1200, 1500, 1700, 900, 1100, 1300, 2000, 1900, 2200]
    }
)
