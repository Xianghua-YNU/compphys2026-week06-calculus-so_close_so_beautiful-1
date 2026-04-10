import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11


def gauss_legendre_2d(func, ax: float, bx: float, ay: float, by: float, n: int = 40) -> float:
    # D1: 二维高斯-勒让德积分
    x, wx = np.polynomial.legendre.leggauss(n)
    y, wy = np.polynomial.legendre.leggauss(n)

    x = 0.5 * (bx - ax) * x + 0.5 * (ax + bx)
    y = 0.5 * (by - ay) * y + 0.5 * (ay + by)

    wx = 0.5 * (bx - ax) * wx
    wy = 0.5 * (by - ay) * wy

    integral = 0.0
    for i in range(n):
        for j in range(n):
            integral += wx[i] * wy[j] * func(x[i], y[j])
    return integral


def plate_force_z(z: float, L: float = 10.0, M_plate: float = 1.0e4, m_particle: float = 1.0, n: int = 40) -> float:
    # D2: 计算方板中心正上方 z 位置的 Fz
    sigma = M_plate / (L ** 2)
    x1, x2 = -L/2, L/2
    y1, y2 = -L/2, L/2

    def integrand(x, y):
        return 1.0 / (x**2 + y**2 + z**2) ** 1.5

    integral = gauss_legendre_2d(integrand, x1, x2, y1, y2, n)
    Fz = G * sigma * m_particle * z * integral
    return Fz


def force_curve(z_values, L: float = 10.0, M_plate: float = 1.0e4, m_particle: float = 1.0, n: int = 40):
    # D3: 返回 z_values 对应的 Fz 数组
    F = np.array([plate_force_z(z, L, M_plate, m_particle, n) for z in z_values])
    return F


# ==================== 自动画图并保存 ====================
if __name__ == "__main__":
    # 不弹出窗口，直接保存图片
    plt.switch_backend('Agg')

    L = 10.0
    M = 1e4
    z_vals = np.linspace(0.2, 10, 50)
    F_vals = force_curve(z_vals, L, M)

    plt.figure(figsize=(8, 4))
    plt.plot(z_vals, F_vals, 'b-', linewidth=2, label='Gravitational force $F_z$')
    plt.xlabel('z (m)')
    plt.ylabel('Force (N)')
    plt.title('Gravitational force above square plate')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('gravity_force.png')
    print("✅ 图片已生成：gravity_force.png")


def force_curve(z_values, L: float = 10.0, M_plate: float = 1.0e4, m_particle: float = 1.0, n: int = 40):
    # D3: 返回 z_values 对应的 Fz 数组
    F = np.array([plate_force_z(z, L, M_plate, m_particle, n) for z in z_values])
    return F
