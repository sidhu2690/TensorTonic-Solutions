import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    return np.array([i if i>= 0 else alpha*i for i in x])