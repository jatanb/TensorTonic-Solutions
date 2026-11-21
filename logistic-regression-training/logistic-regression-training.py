import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(x: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:


    x=np.asarray(x,float)
    y=np.asarray(y,float)
    n,d=x.shape
    w=np.zeros(d)
    b=0.0

    for i in range(steps):
        logit=x@w+b

        prob=_sigmoid(logit)

        w_t=x.T@(prob-y)/n
        b_t=np.mean(prob-y)

        w=w-lr*w_t
        b=b-lr*b_t

    return w,b