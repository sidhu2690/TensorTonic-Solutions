import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    x = np.sort(np.array(x))
    r = np.array(q)/100 * (len(x) - 1)
    l , u= np.floor(r).astype(int), np.ceil(r).astype(int)
    w = r - l
    return (1 - w)*x[l] + w*x[u]
    
    