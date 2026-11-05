import pandas as pd
import sqlite3

# łączenie z bazą danych

try:
    conn = sqlite3.connect("baza.db")
    # tabela = """CREATE TABLE IF NOT EXISTS orders (
    # id INTEGER PRIMARY KEY,
    # customer TEXT,
    # total REAL
    # )
    # """
    #
    # conn.execute(tabela)
    # conn.commit()

    insert = """INSERT INTO orders (
    id, customer, total) VALUES (1, 'Radek', 1000);
    """
    # conn.execute(insert)
    # conn.commit()

    df = pd.read_sql_query("SELECT * FROM orders;", conn)
    print(df)
    print(df.info())
except sqlite3.Error as e:
    print("Bład:", e)
finally:
    if conn:
        conn.close()


#    id customer   total
# 0   1    Radek  1000.0

# Data columns (total 3 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   id        1 non-null      int64
#  1   customer  1 non-null      str
#  2   total     1 non-null      float64
# dtypes: float64(1), int64(1), str(1)
# memory usage: 156.0 bytes
# None