# pliki csv
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

# csv - dane odddzielone znakiem podziału -> ,;tab|

import csv

row = ['radek', 'coe', "3", 0]
columns = ['name', 'branch', 'year', 'cgpa']

filename = 'records.csv'

# newline="" ominięcie problemu znaku końca linii
with open(filename, "w", newline="") as csv_f:
    csv_writer = csv.writer(csv_f)

    csv_writer.writerow(columns)
    csv_writer.writerow(row)

dict_name = dict(zip(columns, row))
print(dict_name)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}
print(type(dict_name))  # <class 'dict'>

filename = 'records_dict.csv'

with open(filename, "w", newline="") as csv_f:
    # csv_writer = csv.DictWriter(csv_f, fieldnames=columns)
    csv_writer = csv.DictWriter(csv_f, fieldnames=dict_name.keys())

    csv_writer.writeheader()  # nagłówki
    csv_writer.writerow(dict_name)
