import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("linregcooling.csv")

X = df[["RoomTemp", "InitialWaterTemp"]]
y = df["TempAfter45min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

preds = model.predict(X_test)

print(preds)

print("MSE: ", mean_squared_error(y_test, preds))
print("R2:", r2_score(y_test, preds))


