from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    stratify=y,
    random_state=42
)

glebokosc = 2

modele = {
    "Jedno drzewo": DecisionTreeClassifier(
        max_depth=glebokosc, random_state=42
    ),
    "Las losowy": RandomForestClassifier(
        n_estimators=40, max_depth=glebokosc, random_state=42
    ),
    "XGBoost": XGBClassifier(
        n_estimators=40, max_depth=glebokosc,
        learning_rate=0.1, random_state=42
    )
}

for nazwa, model in modele.items():
    model.fit(X_train, y_train)
    trening = model.score(X_train, y_train)
    test = model.score(X_test, y_test)
    print(f"{nazwa:14} | trening: {trening:6.1%} | test: {test:6.1%}")

# n_estimators=20
# Jedno drzewo   | trening:  96.4% | test:  92.1%
# Las losowy     | trening:  96.4% | test:  92.1%
# XGBoost        | trening:  98.2% | test:  92.1%

# n_estimators=40
# Jedno drzewo   | trening:  96.4% | test:  92.1%
# Las losowy     | trening:  96.4% | test:  92.1%
# XGBoost        | trening:  99.1% | test:  94.7%
