import numpy as np
import matplotlib.pyplot as plt

a = 6.0  # Box size
Ng = 200  # Number of grid points
Nn = 5  # Number of states

x_g = np.linspace(-a, a, Ng)
dx = x_g[1] - x_g[0]

vext_g = 0.5 * x_g**2  # External potential

T_gg = np.zeros((Ng, Ng))  # Kinetic operator
for i in range(Ng):
    T_gg[i, i] = -2.0
    if i > 0:
        T_gg[i, i - 1] = 1.0
        T_gg[i - 1, i] = 1.0
T_gg *= -0.5 / dx**2

# eigh calculates eigenvalues of a Hermitian matrix;
# these are known to be >= 0.
# eigh returns the eigenvalues sorted, smallest first.
eps_n, psi_gn = np.linalg.eigh(T_gg)

print(eps_n[:Nn])

for i in range(Nn):
    plt.plot(x_g, psi_gn[:, i],
             label='n={}, e={:3f}'.format(i + 1, eps_n[i]))
plt.legend(loc='lower right')
plt.savefig('particles_in_box.pdf')


# Now the harmonic oscillator:
H_gg = T_gg + np.diag(0.5 * x_g**2)
eps_n, psi_gn = np.linalg.eigh(H_gg)

print(eps_n[:Nn])

plt.figure()
for i in range(Nn):
#for i, psi_g in enumerate(psi_gn[:, :Nn].T):
    plt.plot(x_g, psi_g,
             label='n={}, e={:3f}'.format(i + 1, eps_n[i]))
plt.legend(loc='best')
plt.savefig('harmonic_oscillator.pdf')

plt.show()
