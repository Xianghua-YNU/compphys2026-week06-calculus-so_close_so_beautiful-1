import numpy as np

def ring_potential(x, y, z, lambda_, a, eps0=8.854e-12):
    k = 1.0 / (4 * np.pi * eps0)
    r = np.sqrt(x**2 + y**2 + z**2)
    
    # 奇点安全处理（必须加！）
    if r < 1e-10:
        return k * lambda_ * 2 * np.pi * a / a
    
    return k * lambda_ * 2 * np.pi * a / r

# ✅ 关键修复：形状顺序 (len(zs), len(ys))
def potential_grid(xs, ys, zs, lambda_, a, eps0=8.854e-12):
    # 固定 x=0
    V = np.zeros((len(zs), len(ys)))  # 👈 这行是关键！
    
    for i, z in enumerate(zs):
        for j, y in enumerate(ys):
            V[i, j] = ring_potential(0.0, y, z, lambda_, a, eps0)
    
    return V