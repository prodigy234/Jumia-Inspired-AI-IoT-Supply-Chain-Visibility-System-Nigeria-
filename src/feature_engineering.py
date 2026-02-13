from sklearn.preprocessing import LabelEncoder

def engineer_features(df):
    traffic_map = {'Low': 0, 'Medium': 1, 'High': 2}
    df['Traffic_Level_Encoded'] = df['Traffic_Level'].map(traffic_map)

    categorical_cols = [
        'Courier_Type', 'Warehouse_Hub',
        'State', 'City', 'Category', 'Payment_Method'
    ]

    encoder = LabelEncoder()
    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    features = [
        'Delivery_Distance_km',
        'Delivery_Days',
        'Shipment_Temperature_C',
        'Traffic_Level_Encoded',
        'Courier_Type',
        'Warehouse_Hub',
        'State',
        'City',
        'Category',
        'Payment_Method'
    ]

    X = df[features]
    y = df['Delay_Risk_Flag']

    return X, y