import numpy as np

def sample_var_std(x: list) -> dict:
    x = np.array(x)
    s2 = 1/(len(x) - 1) * np.sum((x - np.mean(x))**2)
    return {"variance": float(s2), "standard_deviation": float(s2**0.5)}