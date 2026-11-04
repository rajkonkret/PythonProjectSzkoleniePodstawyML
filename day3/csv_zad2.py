import csv

# filename = "records.csv"
filename = "records_products.csv"

columns = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))  # wykrycie znaku podziału
    print(dialect.delimiter)  # ;

    # StopIteration - skonczyły się dane
    csv_f.seek(0)  # wracamy na początek pliku

    # csv_reader = csv.reader(csv_f)
    # csv_reader = csv.reader(csv_f, delimiter=";")
    csv_reader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csv_reader)  # <_csv.reader object at 0x0000020346F186A0>

    columns = next(csv_reader)  # odczytuje linie i ustawia odczyt na następną

    for row in csv_reader:
        rows.append(row)

print("Columns:", columns)
print("Rows:", rows)
# Columns: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
# ;
# <_csv.reader object at 0x00000247B4D9ACE0>
# Columns: ['sku', 'price']
# Rows: [['1', '200'], ['2', '300'], ['3', '400'], ['4', '700'], ['5', '1200']]
