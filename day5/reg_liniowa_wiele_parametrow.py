import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

reg_df = load_diabetes(as_frame=True).frame

# 10 zmiennych wejsciowych
reg_X = reg_df.drop(columns="target")
reg_y = reg_df["target"]

# podziąl na dane testowe i treningowe
reg_X_train, reg_X_val, reg_y_train, reg_y_val = train_test_split(
    reg_X, reg_y,
    test_size=0.2,
    # random_state=42
    random_state=10
)

# budowa modelu
reg_model = LinearRegression()
reg_model.fit(reg_X_train, reg_y_train)

reg_y_pred = reg_model.predict(reg_X_val)

print(reg_y_pred[:5])

# MAE - Średni błąd bezwzględny im mniejszy tym lepiej
# r2 - współczynnik determinacji, 1 oznacza idealne dopasowanie
# MSE - Średni kwadrat błedów
# RMSE - pierwiastek z MSE

print("MAE:", mean_absolute_error(reg_y_val, reg_y_pred))
print("R2:", r2_score(reg_y_val, reg_y_pred))
# MAE: 42.79610243417211
# R2: 0.5341988244945843