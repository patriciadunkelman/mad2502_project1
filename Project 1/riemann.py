import numpy as np

def left_endpoint(x_vals: np.array, func: np.ufunc):
    approx = 0
    n = len(x_vals) - 1
    for i in range(n):
        area = func(x_vals[i]) * (x_vals[i + 1] - x_vals[i])
        approx += area
    return approx

def trapezoid(x_vals: np.array, func: np.ufunc):
    return 1

def simpson(x_vals: np.array, func: np.ufunc):
    return 1

