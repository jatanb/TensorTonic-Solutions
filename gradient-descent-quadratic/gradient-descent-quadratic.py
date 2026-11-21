def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:

   

    x=0

  


    for _ in range(steps):

        dfx=2*a*x0 + b

        x=x0-lr*dfx

        x0=x

    return x
        