import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from src.data_processing import load_and_clean_data
from src.feature_engineering import engineer_features

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Jumia_Nigeria_Supply_Chain_Dataset.xlsx")
MODEL_PATH = os.path.join(BASE_DIR, "models", "delay_model.pkl")

def train():

    df = load_and_clean_data(DATA_PATH)
    X, y, encoders = engineer_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_test, predictions))

    print("\nROC AUC Score:", roc_auc_score(y_test, probabilities))

    joblib.dump(model, MODEL_PATH)

    print("\nModel saved successfully!")

if __name__ == "__main__":
    train()