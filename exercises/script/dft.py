import numpy as np
import matplotlib.pyplot as plt

xmax = 6.0  # Box size
Ng = 200  # Number of grid points
Nn = 3  # Number of states in our calculation
# (The number of electrons is twice the number of
#  states -- each state is double occupied.)

x_g = np.linspace(-xmax, xmax, Ng)
dx = x_g[1] - x_g[0]

vext_g = 0.5 * x_g**2  # External potential

T_gg = np.zeros((Ng, Ng))  # Kinetic operator
for i in range(Ng):
    T_gg[i, i] = -2.0
    if i > 0:
        T_gg[i, i - 1] = 1.0
        T_gg[i - 1, i] = 1.0
T_gg *= -0.5 / dx**2

# Initialize density as even:
n_g = 2.0 * Nn / (Ng * dx) * np.ones(Ng)
print('Initial charge', n_g.sum() * dx)

# Nn states, each one doubly occupied.
# Initialize as constant density:
vhartree_g = np.zeros(Ng)
vx_g = np.zeros(Ng)


def soft_poisson_solve(n_g):
    vhartree_g = np.zeros(Ng)
    for i in range(Ng):
        for j in range(Ng):
            vhartree_g[i] += n_g[j] / np.sqrt(1.0 + (x_g[i] - x_g[j])**2)
    vhartree_g *= dx
    Ehartree = 0.5 * (vhartree_g * n_g).sum() * dx
    return Ehartree, vhartree_g


def calculate_exchange(n_g):
    vx_g = -(3.0 / np.pi * n_g)**(1.0 / 3.0)
    Ex_prefactor = -3.0 / 4.0 * (3.0 / np.pi)**(1.0 / 3.0)
    Ex = Ex_prefactor * (n_g**(4.0 / 3.0)).sum() * dx
    return Ex, vx_g


density_change = 1.0
while density_change > 1e-6:
    # Calculate Hamiltonian
    veff_g = vext_g + vhartree_g + vx_g
    H_gg = T_gg + np.diag(veff_g)  # Hamiltonian

    # Solve KS equations
    eps_n, psi_gn = np.linalg.eigh(H_gg)
    print('Energies', ' '.join('{:4f}'.format(eps)
                               for eps in eps_n[:Nn]))

    # Normalize states.  The states are normalized
    # already, but not in our dx metric
    psi_gn /= np.sqrt(dx)

    # Update density
    nold_g = n_g
    n_g = 2.0 * (psi_gn[:, :Nn]**2).sum(axis=1)
    density_change = np.abs(nold_g - n_g).sum() * dx

    charge = n_g.sum() * dx
    print('Number of electrons', charge)
    print('Convergence err', density_change)
    assert abs(charge - 2.0 * Nn) < 1e-14

    # Calculate Hartree potential
    Ehartree, vhartree_g = soft_poisson_solve(n_g)
    print('Electrostatic energy', Ehartree)

    # Calculate exchange potential
    # (we won't bother with correlation!)
    Ex, vx_g = calculate_exchange(n_g)
    print('Exchange energy', Ex)

    Ebs = 2.0 * eps_n[:Nn].sum()  # "Band structure" energy
    Ekin = Ebs - (veff_g * n_g).sum() * dx
    print('Ekin', Ekin)
    Epot = Ehartree + Ex + (vext_g * n_g).sum() * dx
    print('Epot', Epot)
    Etot = Ekin + Epot
    print('Energy', Etot)


for i in range(Nn):
    plt.plot(x_g, psi_gn[:, i],
             label='n={}, e={:3f}'.format(i + 1, eps_n[i]))
    plt.legend(loc='lower right')
plt.show()
