import numpy as np

def ring_potential(x, y, z, lambda_, a, eps0=8.854e-12):
    k = 1 / (4 * np.pi * eps0)
    r = np.sqrt(x**2 + y**2 + z**2)
    
    # 奇点处理（核心！）
    if r < 1e-10:
        return k * lambda_ * 2 * np.pi * a / a
    
    V = k * lambda_ * 2 * np.pi * a / r
    return V

# 关键修复：返回形状 (len(zs), len(ys)) 而不是 (len(ys), len(zs))
def potential_grid(xs, ys, zs, lambda_, a, eps0=8.854e-12):
    # 形状顺序：Z 在前，Y 在后！！！
    V = np.zeros((len(zs), len(ys)))
    
    for i, z in enumerate(zs):
        for j, y in enumerate(ys):
            x = 0.0  # 固定x=0平面
            V[i, j] = ring_potential(x, y, z, lambda_, a, eps0)
    return V