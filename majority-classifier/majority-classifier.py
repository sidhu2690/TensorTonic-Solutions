import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    x = y_train[0]
    for i in set(y_train):
        if y_train.count(i) > y_train.count(x):
            x = i
    return np.array([x]*len(X_test))