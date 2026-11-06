import pandas as pd
from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

bmi_diabetes = load_diabetes(as_frame=True)
bmi_df = bmi_diabetes.frame

print(bmi_df.head())
print(bmi_df.shape)
print(bmi_df.describe())

bmi_X = bmi_df[['bmi']]
bmi_y = bmi_df["target"]

# podziąl na dane testowe i treningowe
bmi_X_train, bmi_X_val, bmi_y_train, bmi_y_val = train_test_split(
    bmi_X, bmi_y,
    test_size=0.2,
    # random_state=42
    random_state=10
)

# budowa modelu
bmi_model = LinearRegression()
bmi_model.fit(bmi_X_train, bmi_y_train)

print("Współczynnik:", bmi_model.coef_)
print("Intercept:", bmi_model.intercept_)

# predykcja
bmi_y_pred = bmi_model.predict(bmi_X_val)

bmi_wyniki = pd.DataFrame({
    "Rzeczywiste": bmi_y_val.to_numpy(),
    "Przewidywane": bmi_y_pred
})

print(bmi_wyniki.head(10))

plt.figure(figsize=(9, 5))

plt.scatter(bmi_X_val['bmi'], bmi_y_val, label="Dane rzeczywiste")
plt.scatter(bmi_X_val['bmi'], bmi_y_pred, label="Dane predykcja")

plt.xlabel("BMI - cecha przeskalowana")
plt.ylabel("Wskażnik postępu choroby")
plt.title("Regresja liniowa")
plt.legend()
plt.show()
