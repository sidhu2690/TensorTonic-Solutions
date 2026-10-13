import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    tot = (np.array(x)-np.array(y)).tolist()
    d = [x if x>0 else -x for x in tot]
    return float(sum(d))
    