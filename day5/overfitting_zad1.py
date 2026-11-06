import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

rng = np.random.default_rng(42)

# jedna cecha, wiek roweru w latach
wiek = rng.uniform(0, 10, size=200)
X = wiek.reshape(-1, 1)

# cena wolniej spada wraz z wiekiem
y = 500 + 2000 * np.exp(-0.4 * wiek) + rng.normal(0, 150, size=200)

reg_X_train, reg_X_val, reg_y_train, reg_y_val = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

for glebokosc in [2, 5, 10, None]:
    model = DecisionTreeRegressor(max_depth=glebokosc, random_state=42)
    model.fit(reg_X_train, reg_y_train)

    print(f"Limit: {glebokosc} | "
          f"R2 trening: {model.score(reg_X_train, reg_y_train):.3f} | "
          f"R2 walidacja: {model.score(reg_X_val, reg_y_val)}"
          )
