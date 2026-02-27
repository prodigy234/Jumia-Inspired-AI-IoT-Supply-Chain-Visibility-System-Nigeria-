import pandas as pd

def load_and_clean_data(path):

    df = pd.read_excel(path)

    df = df.drop_duplicates()

    # Handle missing numeric values
    numeric_cols = [
        "Delivery_Distance_km",
        "Delivery_Days",
        "Shipment_Temperature_C"
    ]

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Handle missing categorical
    df["Traffic_Level"] = df["Traffic_Level"].fillna("Medium")

    # Encode target
    df["Delay_Risk_Flag"] = df["Delivery_Status"].apply(
        lambda x: 1 if x == "Delayed" else 0
    )

    return df