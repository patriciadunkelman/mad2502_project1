import numpy as np

def left_endpoint(x_vals: np.array, func: np.ufunc):
    """
    This function approximates the Riemann integral of a function using the left endpoint method.

    The values of the np.array given as x_vals provides the endpoints for our calculations. These x_vals are used to find the
    area. The area between each left endpoint is summed together to find the Riemann approximation.

    Parameters
    -------------
    x_vals : np.array
        Endpoints with which we compute the area of rectangles
    func : np.ufunc
        The function that x_vals are ran through to compute the height of the func at given x inputs

    Returns
    -------------
    float
        The area of the final Riemann approximation
    """
    approx = 0      # Records our sum of areas
    n = len(x_vals)     # This value will be used for the range of our for loop
    for i in range(n-1):    # Range of n - 1 to ensure we don't index outside of the np.array
        area = func(x_vals[i]) * (x_vals[i + 1] - x_vals[i])    # Area = Height(left endpoint) * Width(right endpoint - left endpoint)
        approx += area  #   Add area to our approximation
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

x_vals = np.linspace(0, np.pi, 10000)
func = np.sin