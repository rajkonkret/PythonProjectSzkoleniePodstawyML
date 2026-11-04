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

jedynki = np.ones(5)
print(jedynki)  # [1. 1. 1. 1. 1.]
print(jedynki.dtype)  # float64
print(jedynki.shape)  # (5,)

zakres = np.arange(1, 11)  # od 1 do 10
print(zakres)  # [ 1  2  3  4  5  6  7  8  9 10]

tablica2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print(tablica2d)
# [[1 2 3]
#  [4 5 6]]
print(tablica2d.shape)  # (2, 3)

print(tablica2d[1, 2])  # 6, wiersz drugi (indeks 1) kolumna 3 (indeks 2)

# random
losowe = np.random.random(5)
print(losowe)
# [0.20319649 0.76956343 0.89105657 0.05310144 0.2485744 ]
print(losowe.dtype)  # float64

losowe_int = np.random.randint(1, 50, 5)
print(losowe_int)  # [14 31 49 39 49]

tablica_1 = np.random.randint(1, 50, 100)
print(tablica_1)

# statystyki

# średnia
# gdy w danych bęzie NaN, wynik NaN
print(np.mean(tablica_1))  # 23.64

print(np.nanmean(tablica_1))  # pomija NaN, 24.59

# mediana
# wartośc środkowa
print(np.median(tablica_1))  # 26.0

# odchylenie standardowe
print(np.std(tablica_1))  # 12.47756386479348

print(np.min(tablica_1))  # 1 minimalna
print(np.max(tablica_1))  # 49 maksymalna

# filtrowanie danych
print(tablica_1[tablica_1 > 25])
# [39 42 30 28 39 47 39 32 33 38 27 39 34 48 48 44 26 26 46 32 36 43 40 45
#  39 35 33 32 42 32 46 29 43 39 34 40 48 31 40 35 40 33 28 46]

# przykłąd analizy
sprzedaz = np.array([120, 135, 98, 150, 180, 110, 95, 210, 170, 140])

print("Mediana:", np.median(sprzedaz))
print("Średnia:", np.mean(sprzedaz))
print("Minimum:", np.min(sprzedaz))
print("MAksimum:", np.max(sprzedaz))
print("Odchylenie:", np.std(sprzedaz))
print("Suma:", np.sum(sprzedaz))
# Mediana: 137.5
# Średnia: 140.8
# Minimum: 95
# MAksimum: 210
# Odchylenie: 35.50718237202158
# Suma: 1408

# duża sprzedaż -> większa od średniej
duza_sprzedaz = sprzedaz[sprzedaz > np.mean(sprzedaz)]
print(duza_sprzedaz)  # [150 180 210 170]

# ile razy byłą duża sprzedaz
dni_duzej_sprzedazy = len(duza_sprzedaz)
print(dni_duzej_sprzedazy)  # 4 razy

# dodac 10% do sprzedazy
# broadcasting
wzrost_sprzedazy = sprzedaz * 1.10
print(wzrost_sprzedazy)
# [132.  148.5 107.8 165.  198.  121.  104.5 231.  187.  154. ]

duza_sprzed_mod = [liczba * 1.1 for liczba in sprzedaz]
print(duza_sprzed_mod)
# [np.float64(132.0), np.float64(148.5), np.float64(107.80000000000001),
# np.float64(165.0), np.float64(198.00000000000003), np.float64(121.00000000000001),
# np.float64(104.50000000000001),
# np.float64(231.00000000000003), np.float64(187.00000000000003), np.float64(154.0)]

# 3 sklepy, 4 miesiące
sprzedaz = np.array(
    [
        [120, 130, 140, 150],
        [100, 110, 115, 125],
        [200, 190, 210, 220],
    ]
)

print(sprzedaz)
# [[120 130 140 150]
#  [100 110 115 125]
#  [200 190 210 220]]

# suma dla kazdego sklepu
print(np.sum(sprzedaz[0]))

suma_sklepy_wiersze = sprzedaz.sum(axis=1)  # per sklep
print("Suma dla każdego sklepu:", suma_sklepy_wiersze)
# Suma dla każdego sklepu: [540 450 820]

# suma dla każdego miesiąca
suma_sklepy_kolumna = sprzedaz.sum(axis=0)  # per miesiąc
print("Suma dla każdego miesiąca:", suma_sklepy_kolumna)
# Suma dla każdego miesiąca: [420 430 465 495]

# suma wszystkich
suma_sklepy_wszystkie = sprzedaz.sum()  # sumuje wszytskie wartości
print("Suma dla wszystkich:", suma_sklepy_wszystkie)  # Suma dla wszystkich: 1810

# najlepszy sklep
print(np.max(suma_sklepy_wiersze))  # 820
najlepszy_sklep = np.argmax(suma_sklepy_wiersze)  # poda index
print("Najlepszy sklep nr:", najlepszy_sklep + 1)
# Najlepszy sklep nr: 3

# statystyka bez numpy
import statistics as st

pensja = [5400, 550, 6000, 30000]
print(st.mean(pensja))
print(st.median(pensja))
print(st.mode(pensja))  # dominanta - najczęściej występująca
# 10487.5
# 5700.0
# 5400

# lista w liscie
# zrobic tablice numpy
# wypisać kształt

lista = [[5, 6], [7, 8]]
b = np.array(lista)
print(b)
print(b.shape)
# [[5 6]
#  [7 8]]
# (2, 2)

# ravel() - spłaszczenie
print(b.ravel())  # zwraca nową tablicę, [5 6 7 8]
print(b)  # oryginał bez zmian
# [[5 6]
#  [7 8]]

arr = np.arange(12)  # od 0 do 11
print(arr)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

new_arr = arr.reshape(4, 3)
print(new_arr)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# new_arr = arr.reshape(5, 3) # ValueError: cannot reshape array of size 12 into shape (5,3)

print(new_arr.transpose())
# [[ 0  3  6  9]
#  [ 1  4  7 10]
#  [ 2  5  8 11]]

arr10 = np.arange(1, 10).reshape(3, 3)
print(arr10)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

arr_split = np.split(arr10, 3)
print(arr_split)
# [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]

arr_hsplit = np.hsplit(arr10, 3)
print(arr_hsplit)
# [array([[1],
#        [4],
#        [7]]), array([[2],
#        [5],
#        [8]]), array([[3],
#        [6],
#        [9]])]
