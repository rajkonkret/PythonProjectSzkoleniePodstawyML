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


