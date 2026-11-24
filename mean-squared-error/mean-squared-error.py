import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:

    ans=0

    for i in range(len(y_pred)):
        ans+=(y_pred[i]-y_true[i])**2

    return float(ans)/len(y_pred)
        