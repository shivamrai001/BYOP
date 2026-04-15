import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# Load dataset
data = pd.read_csv('data.csv')

# Features and target
X = data[['Rainfall', 'Fertilizer', 'Temperature']]
y = data['Yield']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Print sample predictions
print("Sample Predictions:")
for i in range(5):
    print(f"Predicted: {predictions[i]:.2f}, Actual: {y_test.iloc[i]:.2f}")

# Graphs
plt.scatter(data['Rainfall'], data['Yield'])
plt.xlabel("Rainfall")
plt.ylabel("Yield")
plt.title("Rainfall vs Yield")
plt.show()

plt.scatter(data['Fertilizer'], data['Yield'])
plt.xlabel("Fertilizer")
plt.ylabel("Yield")
plt.title("Fertilizer vs Yield")
plt.show()

# User input
rain = float(input("Enter Rainfall: "))
fert = float(input("Enter Fertilizer: "))
temp = float(input("Enter Temperature: "))

result = model.predict([[rain, fert, temp]])
print(f"Predicted Crop Yield: {result[0]:.2f}")
# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Show coefficients
print("\nFeature Importance:")
for name, coef in zip(['Rainfall', 'Fertilizer', 'Temperature'], model.coef_):
    print(f"{name}: {coef:.2f}")
