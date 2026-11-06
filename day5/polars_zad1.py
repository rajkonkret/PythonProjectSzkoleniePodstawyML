import time
import polars as pl
import numpy as np
import pandas as pd

N = 10_000_000
a = np.random.randint(0, 100, size=N)
b = np.random.rand(N)

# pandas
df_pd = pd.DataFrame({"a": a, "b": b})
start = time.perf_counter()
mean_pd = df_pd[df_pd["a"] > 50]["b"].mean()
time_pd = time.perf_counter() - start
print(f"Pandas: {time_pd} s")

# polars
df_pl = pl.DataFrame({"a": a, "b": b})
start = time.perf_counter()
mean_pl = df_pl.filter(pl.col("a") > 50)["b"].mean()
time_pl = time.perf_counter() - start
print(f"Polars: {time_pl} s")

# polars lazy
df_pl = pl.DataFrame({"a": a, "b": b})
start = time.perf_counter()
mean_lazy = (df_pl.lazy()
             .filter(pl.col("a") > 50)
             .select(pl.col("b").mean())
             .collect()
             .item()
             )
time_pl = time.perf_counter() - start
print(f"Polars (lazy): {time_pl} s")
print("Wynik:", mean_lazy)
# Pandas: 0.14199079998070374 s
# Polars: 0.024361199990380555 s
# Polars (lazy): 0.007562000013422221 s
# Wynik: 0.5000114419055764
