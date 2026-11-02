tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
# Return a copy of the string converted to uppercase.
tekst.upper()
print(tekst)  # Witaj Świecie

print(tekst.upper())
zmienna = tekst.upper()  # WITAJ ŚWIECIE
print(zmienna)  # WITAJ ŚWIECIE

# lower(), capitalize(), title()
print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.title())  # Witaj Świecie

print(tekst)  # Witaj Świecie
print(len(tekst))  # len() - długośc tekstu, 13 liter

# Witaj Świecie
# 0123456789... numerowanie od zera

print(tekst[0])  # "w"
print(tekst[3])  # "a"

print(tekst.index("a"))  # indeks 3

# "e"
print(tekst.index("e"))  # indeks 9
print(tekst.count("e"))  # występuje 2 razy

print(tekst.lower().count("w"))  # występuje 2 razy

# Witaj Świecie
# 0123456789... numerowanie od zera
print(tekst.count("j", 0, 4))  # wystepuje 0 razy, z prawej strony zbiór otwarty -> 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków (spacji) z początku i końca
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>, typ bajtowy
# \xc5\x9a Ś w systemie szesnastkowym w unicode

print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # długosc 5

# Mam na imię ... .
print("Mam na imię " + str(imie) + ".")  # Mam na imię Radek.

print('Mam na imię', imie, ".")
# Mam na imię Radek .

# f-string - wstrzyknięcie zawartości zmiennej do tekstu
tekst_format = f"Mam na imię {imie}."
print(tekst_format)  # Mam na imię Radek.

tekst_format = f"\tMam na imię {imie}.\n Lubię Pythona.\b"
print(tekst_format)
# "    Mam na imię Radek.
#  Lubię Pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

print(f"""   Mam na imię {imie}
i lubię Pythona.
""")

#    Mam na imię Radek
# i lubię Pythona.

"""Komentarz 
wielolinijkowy - docstring - dokumentacji"""

print(print.__doc__)
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

print("Imie:", imie)  # Imie: Radek
print("Imie:", imie, sep="_ _")  # Imie:_ _Radek

print("Radek:", end="-")
print("tomek")  # Radek:-tomek

starszy = "Witaj %s"  # %s - str
print(starszy % imie)  # Witaj Radek

# zabraniam używać
print("Witaj {}".format("Radek"))  # Witaj Radek
