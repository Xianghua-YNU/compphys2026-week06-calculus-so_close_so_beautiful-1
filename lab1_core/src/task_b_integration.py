import math


def debye_integrand(x: float) -> float:
    if abs(x) < 1e-12:
        return 0.0
    ex = math.exp(x)
    return (x**4) * ex / ((ex - 1.0) ** 2)


def trapezoid_composite(f, a: float, b: float, n: int) -> float:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    h = (b - a) / n
    # 计算首尾项 f(a) + f(b)
    result = f(a) + f(b)
    
    # 累加中间项 2 * f(x_k)
    for k in range(1, n):
        x_k = a + k * h
        result += 2 * f(x_k)
        
    return result * h / 2


def simpson_composite(f, a: float, b: float, n: int) -> float:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n % 2 != 0:
        # 如果用户传入奇数，通常做法是自动加 1 变为偶数，或者报错
        # 这里为了严格符合题目要求，强制修正或提示，此处选择自动修正以保证计算继续
        n += 1 

    h = (b - a) / n
    result = f(a) + f(b)
    
    # 循环累加中间点
    for k in range(1, n):
        x_k = a + k * h
        if k % 2 == 0:
            result += 2 * f(x_k) # 偶数点系数为 2
        else:
            result += 4 * f(x_k) # 奇数点系数为 4
            
    return result * h / 3


def debye_integral(T: float, theta_d: float = 428.0, method: str = "simpson", n: int = 200) -> float:
    if T <= 0:
        return 0.0 # 绝对零度时积分为 0
        
    y= theta_d / T
    
    if method == "trapezoid":
        return trapezoid_composite(debye_integrand, 0, y, n)
    elif method == "simpson":
        return simpson_composite(debye_integrand, 0, y, n)
    else:
        raise ValueError(f"Unknown method: {method}. Use 'trapezoid' or 'simpson'.")