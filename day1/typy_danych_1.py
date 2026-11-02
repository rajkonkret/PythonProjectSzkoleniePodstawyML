import sys

wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.02319842053307009 -> float
print(rok / wiek)  # 43.1063829787234
print(rok // wiek)  # 43 częśc całkowita

print(rok % wiek)  # modulo, reszta z dzielenia 5

print(43 * 47)
print(2026 - 2021)  # 5

print(10 % 3)  # 1

print(wiek ** rok)  # potęgowanie

print(len(str(wiek ** rok)))  # 3388

# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit
# print(len(str(wiek ** rok ** 2)))  #

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# bład zaokrąglenia
print(0.2 + 0.8)  # 1.0 float
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004
#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - pomaga rozwiązac problem zaokrąglenia

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)


# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_python = True
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'> boolean, logiczny
