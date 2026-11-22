import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    x=np.asarray(X,dtype=float)
    y=np.asarray(y,dtype=float)

    w=np.linalg.inv((x.T@x))@x.T@y

    return w