import numpy as np
import matplotlib.pylab as plt

N = 64
x = np.linspace(-5, 5, N)
h = x[1] - x[0]  # Spacing

y = np.sin(x)

plt.plot(x, y, 'o-', label='sin x')

dydx = (y[1:] - y[:N - 1]) / h

# Stencil is most accurate *between* grid points:
xplushalf = 0.5 * (x[1:] + x[:-1])

# Ignore end points of grid as necessary:
d2ydx2 = (y[2:] -2.0 * y[1:-1] + y[:-2]) / h**2

plt.plot(xplushalf, dydx, 's-', label='dy / dx')
plt.plot(x[1:-1], d2ydx2, 'v-', label='d²y / dx²')

T = np.zeros((N, N))
for i in range(N - 1):
    T[i, i] = -2.0
    T[i, i + 1] = 1.0
    T[i + 1, i] = 1.0
T[-1, -1] = -2.0
T *= -0.5 / h**2

Ty = np.dot(T, y)

# Derivative will be discontinuous at the end of the grid
# unless it approaches zero there.  Plot only the interiour:
plt.plot(x[1:-1], Ty[1:-1], 'd-', label='Ty')
print(T)

plt.legend()
plt.show()
