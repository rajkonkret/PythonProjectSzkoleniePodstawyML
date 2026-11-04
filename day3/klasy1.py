# klasa - przepis, szablon
# obiekt - zbudowany wg przepisu
# paradygmaty programowania obiektowego
#  hibernacja, dziedziczenie, polimorfizm, abstrakcja

# pydoc
class User:
    """Komentarz - dokumentacja"""

    def __init__(self, name, id):
        """
        Metoda inicjalizująca - (konstruktor)
        :param name:
        :param id:
        """
        self.name = name
        self.id = id

    def powitanie(self):
        print("Nazywma się:", self.name)

    def __str__(self) -> str:
        return f"{self.name} {self.id}"


# cz1 = User() # TypeError: User.__init__() missing 2 required positional arguments: 'name' and 'id'
cz1 = User("Radek", 1)
print(cz1)  # <__main__.User object at 0x0000024952F37230>
# po dopisaniu __str__
# Radek 1
print(cz1.__doc__)  # Komentarz - dokumentacja
print(cz1.id)
print(cz1.name)
# 1
# Radek
cz1.name = "Tomek"
print(cz1.name)
cz1.powitanie()  # Nazywma się: Tomek


class Admin(User):
    """Klasa Admin, dziedziczy po klasie User"""


ad = Admin("Tomek", 1)
print(ad)  # Tomek 1
