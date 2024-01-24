import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.arange(0, 4 * np.pi - 1, 0.1)
sin_curve = np.sin(x)
cos_curve = np.cos(x)

# Create the figure
plt.figure(figsize=(8, 4))

# Plot sin curve
plt.plot(x, sin_curve, label='sin(x)', color='blue')

# Plot cos curve
plt.plot(x, cos_curve, label='cos(x)', color='red')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Function Value')
plt.title('Sin and Cos Curves')
plt.legend()

# Show the figure
plt.show()
