from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()

# Train the data
model.fit(X_train, y_train)

# Test the model
preds = model.predict(X_test)

# Accuracy
print(model.score(X_test, y_test))