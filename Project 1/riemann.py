import numpy as np

def left_endpoint(x_vals: np.array, func: np.ufunc):
    approx = 0
    n = len(x_vals) - 1
    for i in range(n):
        area = func(x_vals[i]) * (x_vals[i + 1] - x_vals[i])
        approx += area
    return approx

def trapezoid(x_vals: np.array, func: np.ufunc):
    i = 0
    temp = [0]
    while i < len(x_vals) - 1:
        value = (func(x_vals[i]) + func(x_vals[i + 1]))/2 * (x_vals[i + 1] - x_vals[i])
        temp += value
        i += 1
    return sum(temp)

def simpson(x_vals: np.array, func: np.ufunc):
    approx = 0
    n = len(x_vals) - 1
    for i in range(n):
        area = (x_vals[i+1] - x_vals[i])/6 * (func(x_vals[i]) + func(x_vals[i+1]) + 4*(func((x_vals[i] + x_vals[i+1])/2)))
        approx += area
    return approx