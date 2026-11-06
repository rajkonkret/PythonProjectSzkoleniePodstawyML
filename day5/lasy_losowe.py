import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.tree import plot_tree

# Cechy: [wiek w latach, roczne zarobki w tys. zł]
X = np.array([
    [22, 24],
    [32, 28],
    [45, 32],
    [58, 36],
    [24, 44],
    [29, 48],
    [36, 44],
    [44, 52],
    [53, 48],
    [61, 56],
    [25, 72],
    [34, 76],
    [47, 84],
    [60, 92],
])

# 1 = przyznana, 0 = odrzucona
y = np.array([
    0, 0, 0, 0,
    0, 0, 1, 1, 1, 1,
    1, 1, 1, 1,
])

las = RandomForestClassifier(
    n_estimators=10,  # liczba drzew
    max_depth=3,  # maksymalna głebkośc każdego drzewa
    criterion='gini',
    random_state=42
)

las.fit(X, y)

# predykcja
osoba = np.array([[30, 40]])
nazwy_klas = ["odrzucona", "przyznana"]

decyzja = las.predict(osoba)[0]
print(f"Decyzja lasu: pożyczka {nazwy_klas[decyzja]}")

for klasa, p in zip(las.classes_, las.predict_proba(osoba)[0]):
    print(f"{nazwy_klas[klasa]}: {p:.0%}")
# odrzucona: 75%
# przyznana: 25%

# pokaż trzy drzewa
fig, osie = plt.subplots(1, 3, figsize=(18, 5))

for numer, (os, drzewo) in enumerate(zip(osie, las.estimators_), start=1):
    plot_tree(
        drzewo,
        feature_names=['wiek', "zarobki"],
        class_names=nazwy_klas,
        filled=True,
        rounded=True,
        ax=os
    )
    os.set_title(f"Drzewo {numer}")

fig.tight_layout()
plt.show()
