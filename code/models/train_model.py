import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load the California housing dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Ensure the models directory exists
model_dir = os.path.join(os.path.dirname(__file__), '../../models')
os.makedirs(model_dir, exist_ok=True)

# Save the model
joblib.dump(model, os.path.join(model_dir, 'california_housing_model.joblib'))
