import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("linreg_housingPrices.csv")

X = df[["size", "rooms"]]
y = df["price"]

n_test = 20

X_train = X.iloc[:-n_test]
y_train = y.iloc[:-n_test]

# Test = last 20 rows
X_test = X.iloc[-n_test:]
y_test = y.iloc[-n_test:]

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(f"Predicted Value: {prediction}")

r2 = r2_score(y_test, prediction)

print("R^2:", r2)


