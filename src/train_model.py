import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from data_preprocessing import load_and_clean_data
from feature_engineering import engineer_features

DATA_PATH = "data/Jumia_Nigeria_Supply_Chain_Dataset.xlsx"

def train():
    df = load_and_clean_data(DATA_PATH)
    X, y = engineer_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test)))

    joblib.dump(model, "models/delay_model.pkl")

if __name__ == "__main__":
    train()