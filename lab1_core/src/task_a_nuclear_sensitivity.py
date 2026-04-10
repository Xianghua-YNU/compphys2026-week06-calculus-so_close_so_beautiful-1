import numpy as np


def rate_3alpha(T: float) -> float:
    T8 = T / 1.0e8
    return 5.09e11 * (T8 ** (-3.0)) * np.exp(-44.027 / T8)


def finite_diff_dq_dT(T0: float, h: float = 1e-8) -> float:
    # TODO A1: 使用前向差分实现 dq/dT
    # 计算相对步长 ΔT = h * T0
    dT = h * T0
    # 计算 q(T0) 和 q(T0 + dT)
    q0 = rate_3alpha(T0)
    q1 = rate_3alpha(T0 + dT)
    # 返回前向差分近似
    return (q1 - q0) / dT

def sensitivity_nu(T0: float, h: float = 1e-8) -> float:
    # TODO A2: 根据 nu = (T/q) * dq/dT 计算温度敏感性指数
    # 计算反应率 q(T0)
    q0 = rate_3alpha(T0)
    # 计算 dq/dT
    dq_dT = finite_diff_dq_dT(T0, h)
    # 返回 ν = (T/q) * dq/dT
    return (T0 / q0) * dq_dT

def nu_table(T_values, h: float = 1e-8):
    # TODO A3: 返回 [(T, nu(T)), ...]
     # 计算每个温度点的ν值
    result = []
    for T0 in T_values:
        nu0 = sensitivity_nu(T0, h)
        result.append((T0, nu0))
    return result
if __name__ == "__main__":
    # 题目要求的必算温度点
    test_temperatures = [1.0e8, 2.5e8, 5.0e8, 1.0e9, 2.5e9, 5.0e9]
    # 批量计算所有温度的敏感性指数
    result_table = nu_table(test_temperatures)
    # 按题目要求的格式输出结果
    print("===== 3-α反应温度敏感性指数计算结果 =====")
    for T, nu in result_table:
        print(f"{T:.3e} K : nu = {nu:.2f}")
    print("==========================================")