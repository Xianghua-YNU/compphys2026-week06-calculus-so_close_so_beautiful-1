import numpy as np

def gauss_legendre_integrate(f, a, b, n=40):
    x, w = np.polynomial.legendre.leggauss(n)
    t = 0.5 * (x + 1) * (b - a) + a
    dt = 0.5 * (b - a)
    integral = np.sum(w * f(t)) * dt
    return integral

def gravitational_force(z, M, R, G):
    if z < 1e-10:
        return 0.0
    def f(theta):
        return (z - R * np.cos(theta)) * np.sin(theta) / (R**2 + z**2 - 2 * R * z * np.cos(theta))**1.5
    integral = gauss_legendre_integrate(f, 0, np.pi, 40)
    F = G * M / (2 * R**2) * integral
    return F