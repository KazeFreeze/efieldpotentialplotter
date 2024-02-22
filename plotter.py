import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
data = pd.read_csv('data.csv', header=None)
x_values = data.iloc[:, 0].values
y_values = data.iloc[:, 1].values
potential_values = data.iloc[:, 2].values

# Calculate electric field components
Ex = np.gradient(potential_values, axis=0)
Ey = np.gradient(potential_values, axis=1)

# Define grid
x_grid = np.linspace(min(x_values), max(x_values), 20)
y_grid = np.linspace(min(y_values), max(y_values), 20)
X, Y = np.meshgrid(x_grid, y_grid)

# Calculate magnitude and direction of electric field
M = np.hypot(Ex, Ey)
U = Ex / M
V = Ey / M

# Plot vector field with colorful settings
fig3, ax3 = plt.subplots()
ax3.set_title("Electric Field Vector Field")
Q = ax3.quiver(X, Y, U, V, M, units='x', pivot='tip', width=0.022, scale=1 / 0.15)
qk = ax3.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E', coordinates='figure')
ax3.scatter(X, Y, color='0.5', s=1)

# Save the plot as JPEG or PNG
plt.savefig('electric_field_plot.jpg')  # Save as JPEG
# plt.savefig('electric_field_plot.png')  # Save as PNG

plt.show()
