import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

housing_demo = pd.DataFrame({
    "metraz": [40, 60, 80, 100],
    "miasto": ["Warszawa", "Kraków", "Warszawa", "Gdańsk"],
    "cena": [450000, 570000, 800000, 920000]
})

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ["metraz"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["miasto"])
])

housing_encoded = preprocessor.fit_transform(housing_demo[["metraz", "miasto"]])

print(housing_encoded)
