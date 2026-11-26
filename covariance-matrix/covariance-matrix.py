import numpy as np

def covariance_matrix(X: list) -> np.ndarray:

    x=np.asarray(X,dtype=float)

    xc=x-np.mean(x,axis=0)

    sigma=xc.T@xc/(x.shape[0]-1)

    return sigma