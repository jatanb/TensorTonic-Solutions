import math

def elu(X: list, alpha: float = 1.0) -> list:

    for i in range(len(X)):
        if X[i]>0:
            continue
        else:
            X[i]=alpha*(math.exp(X[i])-1)

    return X