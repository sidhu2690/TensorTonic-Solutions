import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    w, g, s = np.array(w), np.array(g), np.array(s)
    st = beta * s + (1 - beta) * g**2
    wt = w - lr * g / (st + eps)**0.5
    return wt, st