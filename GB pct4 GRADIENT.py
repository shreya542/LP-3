import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(initial_x, learning_rate, num_iterations):
    x_values = [initial_x]
    y_values = [(initial_x + 3)**2]

    for _ in range(num_iterations):
        gradient = 2 * (initial_x + 3)  # Gradient of the function y = (x + 3)^2
        initial_x = initial_x - learning_rate * gradient

        x_values.append(initial_x)
        y_values.append((initial_x + 3)**2)

    return x_values, y_values

# Set initial parameters
initial_x = 2
learning_rate = 0.1
num_iterations = 50

# Run Gradient Descent
x_values, y_values = gradient_descent(initial_x, learning_rate, num_iterations)

# Print the final local minimum
local_minima_x = x_values[-1]
local_minima_y = y_values[-1]

print(f"Local Minimum: x = {local_minima_x}, y = {local_minima_y}")

# Plot the function and the path taken by Gradient Descent
x = np.linspace(-10, 4, 100)
y = (x + 3)**2

plt.plot(x, y, label='y = (x + 3)^2', color='blue')
plt.scatter(x_values, y_values, color='red', label='Gradient Descent Path')
plt.title('Gradient Descent to Find Local Minimum')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
