import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 500)

x_safe = np.where(x == 0, 1e-8, x)
y = (1 / x_safe) * np.sin(5 * x)

plt.plot(x, y, label='(1/x)*sin(5x)', color='darkred', linewidth=3)

plt.title('Графік функції Y(x) = 1/x * sin(5x)', fontsize=15)

plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')

plt.legend()
plt.grid(True)

plt.show()