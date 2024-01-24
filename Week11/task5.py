import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

# Generate data with noise
noise = np.random.uniform(-20, 20, 100)
x = np.linspace(0, 100, 100) + noise
y = np.linspace(0, 50, 100) + noise

# Scatter plot
plt.scatter(x, y, label='Data with Noise')

# Fit a linear regression line
b, m = polyfit(x, y, 1)
y_pred = m * x + b

# Plot the regression line
plt.plot(x, y_pred, color='red', label='Linear Regression Line')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Linear Regression Line')
plt.legend()

# Show the plot
plt.show()
