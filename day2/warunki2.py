# od pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programmowania: ")

match lang.strip().casefold():
    case "python":
        lista.append("Znam pythona")
    case "java":
        lista.append("Znam Javę")
    case "c":
        lista.append("Znam C")
    case _:  # odpowiednik else
        print("Nie znam")

print(lista)
# Podaj znany Ci język programmowania: java
# ['Znam Javę']

lista1 = [1, 2, 3]

match lista1:
    case [a, b, c]:
        print(a, b, c)  # 1 2 3
