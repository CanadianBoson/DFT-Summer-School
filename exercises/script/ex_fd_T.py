import numpy as np
import matplotlib.pylab as plt

N = 50
x = np.linspace(-5, 5, N)
h = x[1] - x[0]  # Spacing

y = np.sin(x)

plt.plot(x, y, 'o-', label='sin x')

dsindx = (y[1:] - y[:N - 1]) / h
xhalf = 0.5 * (x[1:] + x[:-1])

d2sindx2 = (y[2:] -2.0 * y[1:-1] + y[:-2]) / h**2

plt.plot(xhalf, dsindx, 's-', label='d sin x / dx')
plt.plot(x[1:-1], d2sindx2, 'v-', label='d² sin x / dx²')
plt.legend()
plt.show()
