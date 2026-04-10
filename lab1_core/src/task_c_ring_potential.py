import numpy as np


def ring_potential_point(x: float, y: float, z: float, a: float = 1.0, q: float = 1.0, n_phi: int = 720) -> float:
    # C1: 用离散积分计算单点电势
    phi = np.linspace(0, 2 * np.pi, n_phi)
    r = np.sqrt((x - a * np.cos(phi))**2 + (y - a * np.sin(phi))**2 + z**2)
    integrand = 1.0 / r
    dphi = 2 * np.pi / n_phi
    integral = np.sum(integrand) * dphi
    V = q / (2 * np.pi) * integral
    return V


def ring_potential_grid(y_grid, z_grid, x0: float = 0.0, a: float = 1.0, q: float = 1.0, n_phi: int = 720):
    # C2: 在 yz 网格上计算电势矩阵
    V_grid = np.zeros_like(y_grid)
    ny, nz = y_grid.shape
    for i in range(ny):
        for j in range(nz):
            y = y_grid[i, j]
            z = z_grid[i, j]
            V_grid[i, j] = ring_potential_point(x0, y, z, a, q, n_phi)
    return V_grid


def axis_potential_analytic(z: float, a: float = 1.0, q: float = 1.0) -> float:
    return q / np.sqrt(a * a + z * z)
    # 下面是测试画图代码，不影响主函数
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.switch_backend('Agg')

    a = 1.0
    q = 1.0
    x0 = 0.0

    y = np.linspace(-2, 2, 40)
    z = np.linspace(-2, 2, 40)
    Y, Z = np.meshgrid(y, z)

    V = ring_potential_grid(Y, Z, x0, a, q)
    Ey, Ez = np.gradient(-V, y[1]-y[0], z[1]-z[0])

    plt.figure(figsize=(8, 8))
    plt.contour(Y, Z, V, levels=25, cmap='coolwarm')
    plt.quiver(Y, Z, Ey, Ez, color='k', scale=30)
    circle = np.linspace(0, 2*np.pi, 100)
    plt.plot(a*np.cos(circle), a*np.sin(circle), 'r-', lw=2)
    plt.axis('equal')
    plt.savefig('ring_field.png')
    print("图片已保存为 ring_field.png")