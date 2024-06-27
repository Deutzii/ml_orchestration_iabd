import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load the initial data
file_path = 'data/weather_data-20240627.csv'
df = pd.read_csv(file_path)

# Select relevant features
features = df[['relative_humidity_2m', 'dew_point_2m', 'apparent_temperature', 'precipitation', 'rain', 'snowfall', 'weather_code', 'surface_pressure', 'wind_speed_10m']]
target = df['temperature_2m']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Save the model to a file
joblib.dump(model, 'weather_model.pkl')
