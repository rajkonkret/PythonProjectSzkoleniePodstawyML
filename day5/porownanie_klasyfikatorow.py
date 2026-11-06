import pandas as pd
from matplotlib import pyplot as plt
from sklearn import clone
from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, precision_score, f1_score, \
    recall_score
from sklearn.model_selection import StratifiedKFold, train_test_split, cross_val_predict, cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

SEED = 42

cls_data = load_breast_cancer(as_frame=True)
cls_target = (cls_data.target == 0).astype(int).rename("złośliwy")
cls_X_train, cls_X_test, cls_y_train, cls_y_test = train_test_split(
    cls_data.data, cls_target, test_size=0.25, stratify=cls_target, random_state=SEED
)
cls_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
cls_logistic = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, random_state=SEED))
cls_dummy = DummyClassifier(strategy="most_frequent")


def classification_scores(actual, predicted):
    tn, fp, fn, tp = confusion_matrix(actual, predicted, labels=[0, 1]).ravel()
    return {
        "accuracy": accuracy_score(actual, predicted),
        "precision": precision_score(actual, predicted, zero_division=0),
        "recall": recall_score(actual, predicted, zero_division=0),
        "F1": f1_score(actual, predicted, zero_division=0),
        "TN": tn, "FP": fp, "FN": fn, "TP": tp,
    }


cls_dummy_oof = cross_val_predict(cls_dummy, cls_X_train, cls_y_train, cv=cls_cv)
cls_logistic_oof = cross_val_predict(
    cls_logistic, cls_X_train, cls_y_train, cv=cls_cv, method="predict_proba"
)[:, 1]
cls_logistic_oof_labels = cls_logistic_oof >= 0.5
print(pd.DataFrame({
    "Klasa większościowa": classification_scores(cls_y_train, cls_dummy_oof),
    "Logistyczna 0,50": classification_scores(cls_y_train, cls_logistic_oof_labels),
}).T.round(3))

ConfusionMatrixDisplay.from_predictions(
    cls_y_train, cls_logistic_oof_labels, labels=[0, 1],
    display_labels=["0 · łagodny", "1 · złośliwy"], colorbar=False, cmap="Blues",
)
plt.title("Regresja logistyczna · predykcje OOF · próg 0,50")
plt.tight_layout()
plt.show()
cls_candidates = {
    "Regresja logistyczna": cls_logistic,
    "Drzewo": DecisionTreeClassifier(max_depth=4, min_samples_leaf=5, random_state=SEED),
    "Random forest": RandomForestClassifier(
        n_estimators=150, min_samples_leaf=3, random_state=SEED, n_jobs=1,
    ),
    "XGBoost": XGBClassifier(
        n_estimators=100, max_depth=3, learning_rate=0.08,
        objective="binary:logistic", eval_metric="logloss",
        tree_method="hist", device="cpu", random_state=SEED, n_jobs=1,
    ),
}
cls_cv_rows = []
for cls_name, cls_candidate in cls_candidates.items():
    cls_cv_metrics = cross_validate(
        cls_candidate, cls_X_train, cls_y_train, cv=cls_cv,
        scoring="f1", return_train_score=True, error_score="raise",
    )
    cls_cv_rows.append({
        "model": cls_name,
        "F1 trening": cls_cv_metrics["train_score"].mean(),
        "F1 CV": cls_cv_metrics["test_score"].mean(),
        "odchylenie F1 CV": cls_cv_metrics["test_score"].std(),
    })
cls_cv_results = pd.DataFrame(cls_cv_rows).set_index("model").sort_values("F1 CV", ascending=False)
print(cls_cv_results.round(3))
cls_winner_name = cls_cv_results.index[0]
print("Wybrany według F1 CV:", cls_winner_name)
# %%
cls_test_rows = []
for cls_label, cls_estimator in cls_candidates.items():
    cls_fitted = clone(cls_estimator).fit(cls_X_train, cls_y_train)
    cls_prediction = cls_fitted.predict(cls_X_test)
    cls_test_rows.append({"model": cls_label, **classification_scores(cls_y_test, cls_prediction)})
    if cls_label == cls_winner_name:
        ConfusionMatrixDisplay.from_predictions(
            cls_y_test, cls_prediction, labels=[0, 1],
            display_labels=["łagodny", "złośliwy"], colorbar=False,
        )
        plt.title(f"Test · {cls_label}")
        plt.tight_layout()
        plt.show()

cls_test_table = pd.DataFrame(cls_test_rows).set_index("model")
print(cls_test_table.round(3))
print("Najmniej FN:", ", ".join(cls_test_table.index[cls_test_table["FN"] == cls_test_table["FN"].min()]))
assert (cls_test_table[["TN", "FP", "FN", "TP"]].sum(axis=1) == len(cls_y_test)).all()
assert set(cls_X_train.index).isdisjoint(cls_X_test.index)
print("Kontrole podziałów i wyników przeszły.")
