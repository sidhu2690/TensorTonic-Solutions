import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    mean = np.mean(np.array(X), axis=axis, keepdims=True)
    std = np.std(np.array(X), axis=axis, keepdims=True)
    return (np.array(X) - mean)/np.maximum(std, eps)