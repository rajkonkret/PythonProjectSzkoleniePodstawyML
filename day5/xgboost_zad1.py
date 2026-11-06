from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

iris = load_iris()
X = iris.data  # pomiary każdego kwiatu
y = iris.target  # etykiety 0, 1, 2

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    stratify=y,
    random_state=42
)

# model i trening
model = XGBClassifier(n_estimators=20, max_depth=2, random_state=42)
model.fit(X_train, y_train)

# predykcja
predykcja = model.predict(X_test[:1])[0]
print("Model przewidział:", iris.target_names[predykcja])
print("Prawdziwy gatunek:", iris.target_names[y_test[0]])
print(f"Dokładność na całym teście: {model.score(X_test, y_test):.1%}")

# Model przewidział: setosa
# Prawdziwy gatunek: setosa
# Dokładność na całym teście: 92.1%

model.save_model("model_xgboost.json")

model_load = XGBClassifier()
model_load.load_model("model_xgboost.json")
predykcja = model_load.predict(X_test[:1])[0]
print("Model przewidział:", iris.target_names[predykcja])
print("Prawdziwy gatunek:", iris.target_names[y_test[0]])
print(f"Dokładność na całym teście: {model.score(X_test, y_test):.1%}")
# Model przewidział: setosa
# Prawdziwy gatunek: setosa
# Dokładność na całym teście: 92.1%
# Model przewidział: setosa
# Prawdziwy gatunek: setosa
# Dokładność na całym teście: 92.1%