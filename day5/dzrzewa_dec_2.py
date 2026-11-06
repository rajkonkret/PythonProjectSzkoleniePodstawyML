# pip install -U scikit-learn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree

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

# budowa i trenowanie drzewa
# tree = DecisionTreeClassifier(criterion='gini', max_depth=2)
tree = DecisionTreeClassifier(criterion='gini', max_depth=3)
tree.fit(X, y)

# predykcja
# decision = tree.predict(np.array([[30, 40]])) # Pożyczka odrzucona
decision = tree.predict(np.array([[35, 41]])) # dla depth=3 Pożyczka przyznana
print("Pożyczka przyznana" if decision[0] == 1 else "Pożyczka odrzucona")

# wizualizacja drzewa
plt.figure(figsize=(8, 5))
plot_tree(tree, feature_names=['wiek', 'zarobki'],
          class_names=['odrzucona', 'przyznana'], filled=True)
plt.title("Drzewo decyzyjne: przyznanie pożyczki")
plt.tight_layout()
plt.show()
