# Powerful N-dimensional arrays
# Fast and versatile, the NumPy vectorization,
# indexing, and broadcasting concepts are the de-facto standards of array computing today.
import numpy as np

# pip install numpy

print(np.__version__)  # 2.5.4

liczby = [43, 546, 324, 65, 12, 76, 3, 2345, 456, 788]
print(liczby)
# [43, 546, 324, 65, 12, 76, 3, 2345, 456, 788]

# ndarray
tablica_1 = np.array(liczby)
print(tablica_1)
# [  43  546  324   65   12   76    3 2345  456  788]

# przemnożyc wszystkie elementy tej kolekcji przez 2
print(liczby * 2)
# [43, 546, 324, 65, 12, 76, 3, 2345, 456, 788, 43, 546, 324, 65, 12, 76, 3, 2345, 456, 788]

# broadcasting - wykonanie operacji na kazdym elemencie tablicy
print(tablica_1 * 2)
# [  86 1092  648  130   24  152    6 4690  912 1576]

print(tablica_1 * 3)
# [ 129 1638  972  195   36  228    9 7035 1368 2364]

zera = np.zeros(5)
print(zera)  # [0. 0. 0. 0. 0.]
print(type(zera))  # <class 'numpy.ndarray'>

print(zera.dtype)  # float64

zero2d = np.zeros((4, 5))  # wiersze, kolumny
print(zero2d)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
print(zero2d.dtype)  # float64
print(zero2d.shape)  # kształt (4, 5)

zera_int = np.zeros(5, dtype=int)
print(zera_int)  # [0 0 0 0 0]
print(zera_int.dtype)  # int64

zera_int = np.zeros(5, dtype=np.int64)
print(zera_int)  # [0 0 0 0 0]
print(zera_int.dtype)  # int64
