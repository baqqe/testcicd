import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def load_data(file_path="lego_injection_molding_data.csv"):
    df = pd.read_csv(file_path)
    df = pd.get_dummies(df, columns=["Material_Used", "Shift"], drop_first=True)  # One-hot encoding
    return df

def train_model(data_path="lego_injection_molding_data.csv"):
    df = load_data(data_path)
    X = df.drop(columns=["Mold_ID", "Cycle_Time"])
    y = df["Cycle_Time"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    return model, mse

if __name__ == "__main__":
    model, mse = train_model()
    print(f"Model trained. Mean Squared Error: {mse}")
