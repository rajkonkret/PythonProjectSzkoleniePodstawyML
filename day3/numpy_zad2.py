import numpy as np

# łądowanie pliku do pamięci
input_stock_price_array = np.genfromtxt(
    "AAPL_stock_price_example.csv",
    delimiter=",",
    names=True,  # traktuj pierwszy wiersz jako nazwy kolumn
    usecols=(1,)  # wczytaj kolumnę o indeksie 1
)

print(input_stock_price_array)
# [(157.919998,) (142.190002,) (148.259995,) (147.929993,) (150.75    ,)
#  (153.309998,) (153.800003,) (152.289993,) (150.      ,) (153.070007,)...

# pięc pierwszych
print(input_stock_price_array[:5])
# [(157.919998,) (142.190002,) (148.259995,) (147.929993,) (150.75    ,)]

print(input_stock_price_array.dtype)
# [('Close', '<f8')]
# Close - nazwa kolumna
# <f8 -> float 8bajtowy -> float64

# co drugi element
even = input_stock_price_array[::2]
print(even)

# ile elementów
print(input_stock_price_array.size)  # 229

sorted_stock_price = np.sort(input_stock_price_array)[::-1]  # wodwrotnej kolejnośc
print(sorted_stock_price[:5])
# [(267.100006,) (266.369995,) (266.290009,) (265.76001 ,) (264.470001,)]

# największy element
print(sorted_stock_price[0])  # (267.100006,)
