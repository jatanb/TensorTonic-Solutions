import numpy as np

def ridge_regression(x: list, y: list, lam: float) -> list:
    x=np.asarray(x,dtype=float)
    y=np.asarray(y,dtype=float)
    I = np.identity(len(x[0]))

    calc1=(x.T)@x + lam*I

    w=(np.linalg.inv(calc1))@((x.T)@y)

    return w