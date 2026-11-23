import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    ans=0

    for i in range(len(x)):
        ans+=(x[i]*p[i])

    return float(ans)