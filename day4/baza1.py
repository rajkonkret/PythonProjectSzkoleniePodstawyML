import pandas as pd
import sqlite3

# łączenie z bazą danych

try:
    conn = sqlite3.connect("baza.db")
    tabela = """CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    total REAL
    )
    """

    conn.execute(tabela)
    conn.commit()
except sqlite3.Error as e:
    print("Bład:", e)
finally:
    if conn:
        conn.close()
