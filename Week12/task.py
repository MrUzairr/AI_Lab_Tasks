import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=columns)

# Pre-processing: Remove null and duplicate values
df = df.dropna()
df = df.drop_duplicates()

df.to_csv("linear_regression_results.csv", index=False)
# Display scatter plot of the dataset
plt.scatter(df["sepal_length"], df["sepal_width"], c=pd.factorize(df["class"])[0], cmap="viridis", edgecolor="k")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot of Iris Dataset")
plt.show()

# Split the dataset into train and test sets
train_size = int(0.75 * len(df))
train_data = df.iloc[:train_size]
test_data = df.iloc[train_size:]

# Implement linear regression model (for simplicity, I'll use only one feature)
def linear_regression(X, y, learning_rate, epochs):
    m, b = 0, 0
    n = len(X)

    for _ in range(epochs):
        y_pred = m * X + b
        m_gradient = (-2/n) * sum(X * (y - y_pred))
        b_gradient = (-2/n) * sum(y - y_pred)
        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient

    return m, b

# Fit the model on the training dataset
X_train = train_data["sepal_length"].values
y_train = train_data["sepal_width"].values
m, b = linear_regression(X_train, y_train, learning_rate=0.01, epochs=1000)

# Perform binary classification on the test dataset
X_test = test_data["sepal_length"].values
y_test = m * X_test + b
predicted_class = np.where(y_test > 3.0, "Iris-setosa", "Iris-versicolor")

# Find mean square error
mse = np.mean((y_test - test_data["sepal_width"].values)**2)
print("Mean Square Error:", mse)
