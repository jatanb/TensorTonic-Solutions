import numpy as np

def manhattan_distance(x: list, y: list) -> float:

    ans=0

    for i in range(len(x)):
        ans+=abs(x[i]-y[i])

    return float(ans)

   