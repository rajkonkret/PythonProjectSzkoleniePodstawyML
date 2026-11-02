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
