import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    param, grad, m, v = np.array(param), np.array(grad), np.array(m), np.array(v)
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1-beta2) * grad**2
    mt = m / (1 - beta1**t)
    vt = v / (1 - beta2 ** t)
    theta = param - lr * mt / (vt**(0.5) + eps)
    return theta, m, v