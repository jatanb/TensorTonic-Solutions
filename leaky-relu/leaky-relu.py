import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:

    for i in range(len(x)):
        if x[i]<0:
            x[i]=float(x[i]*alpha)
        else:
            x[i]=float(x[i])

    return np.array(x)
        