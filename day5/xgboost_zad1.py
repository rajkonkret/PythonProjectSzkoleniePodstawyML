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


