import numpy as np
import matplotlib.pyplot as plt

# Q4. Generate x values using np.linspace() from -10 to 10 with 100 points
x = np.linspace(-10, 10, 100)


y1 = x ** 2


y2 = np.sin(x)


y3 = np.exp(x)


y4 = np.log(np.abs(x) + 1)


plt.figure(figsize=(10, 6))

plt.plot(x, y1, label="Y = x^2")

plt.title("Plot of Y = x^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.legend()
plt.show()
