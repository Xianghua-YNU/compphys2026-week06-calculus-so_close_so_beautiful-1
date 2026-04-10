import numpy as np

def ring_potential(x, y, z, lambda_, a, eps0=8.854e-12):
    k = 1 / (4 * np.pi * eps0)
    r = np.sqrt(x**2 + y**2 + z**2)
    cos_theta = (x**2 + y**2 - a**2) / ((x**2 + y**2 + z**2) - a**2) if r != a else 0.0
    E_field = k * lambda_ * a / (r**2 - a**2) * np.sqrt(1 - cos_theta**2)
    V = k * lambda_ * 2 * np.pi * a / np.sqrt(x**2 + y**2 + z**2)
    return V

def potential_grid(X, Y, Z, lambda_, a, eps0=8.854e-12):
    V = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            for k in range(X.shape[2]):
                x = X[i,j,k]
                y = Y[i,j,k]
                z = Z[i,j,k]
                r = np.sqrt(x**2 + y**2 + z**2)
                if r < 1e-10:
                    V[i,j,k] = 0.0
                else:
                    V[i,j,k] = ring_potential(x, y, z, lambda_, a, eps0)
    return V