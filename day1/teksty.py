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
