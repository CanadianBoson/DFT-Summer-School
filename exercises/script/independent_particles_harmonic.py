# This file is identical to independent_particles_free
# except for the lines defining the Hamiltonian
import numpy as np
import matplotlib.pyplot as plt

a = 6.0  # Box size
Ng = 200  # Number of grid points
Nn = 4  # Number of states

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

H_gg = T_gg + np.diag(vext_g)  # Hamiltonian
eps_n, psi_gn = np.linalg.eigh(H_gg)

print(eps_n[:Nn])

for i, psi_g in enumerate(psi_gn[:, :Nn].T):
    plt.plot(x_g, psi_g, label='n={}, e={:3f}'.format(i + 1, eps_n[i]))
    plt.legend(loc='lower right')
plt.show()
