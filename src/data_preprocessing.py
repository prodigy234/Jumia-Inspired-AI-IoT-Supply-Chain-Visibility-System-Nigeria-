import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel(path)

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df['Shipment_Temperature_C'].fillna(df['Shipment_Temperature_C'].mean(), inplace=True)
    df['Traffic_Level'].fillna('Medium', inplace=True)

    # Encode target
    df['Delay_Risk_Flag'] = df['Delivery_Status'].apply(
        lambda x: 1 if x == 'Delayed' else 0
    )

    return df