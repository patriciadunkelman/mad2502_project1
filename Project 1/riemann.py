import numpy as np

def left_endpoint(x_vals: np.array, func: np.ufunc):
    """
    This function approximates the Riemann integral of a function using the left endpoint method.

    The values of the np.array given as x_vals provides the endpoints for our calculations. These x_vals are used to find the
    area. The area between each left endpoint is summed together to find the Riemann approximation.

    Parameters
    ------------
    x_vals : np.array
        Endpoints with which we compute the area of rectangles
    func : np.ufunc
        The function that x_vals are ran through to compute the height of the func at given x inputs

    Returns
    ------------
    float
        The area of the Riemann approximation
    """
    approx = 0      # Records our sum of areas
    n = len(x_vals)     # This value will be used for the range of our for loop
    for i in range(n-1):    # Range of n - 1 to ensure we don't index outside of the np.array
        area = func(x_vals[i]) * (x_vals[i + 1] - x_vals[i])    #Area = height(function output with left endpoint input) * width(right endpoint - left endpoint)
        approx += area  #   Add area to our approximation
    return approx

def trapezoid(x_vals: np.array, func: np.ufunc):
    """
        This function approximates the Riemann integral of a function using the trapezoid method.

        The values of the np.array given as x_vals provides the endpoints for our calculations. These x_vals are used to find the
        area. The area between each endpoint is calcuated by the area of the trapezoid formed by (a,0), (b,0), (a, f(a)), and (b, f(b)).

        Parameters
        ------------
        x_vals : np.array
            Endpoints with which we compute the area of rectangles
        func : np.ufunc
            The function that x_vals are ran through to compute the height of the func at given x inputs

        Returns
        ------------
        float
            The area of the Riemann approximation
        """
    i = 0 # creates i
    temp = [0] # creates the temp list
    while i < len(x_vals) - 1: # runs for each value of x
        value = (func(x_vals[i]) + func(x_vals[i + 1]))/2 * (x_vals[i + 1] - x_vals[i]) # calculates trapezoid area
        temp += value # value to temp
        i += 1 # iterates
    return sum(temp) # sums the list temp

def simpson(x_vals: np.array, func: np.ufunc):
    """
        This function approximates the Riemann integral of a function using the Simpson method.

        The values of the np.array given as x_vals provides the endpoints for our calculations. These x_vals are used to find the
        area. Simpson's method approximates with {b-a}{6}(f(a) + 4f{a+b}/{2}) + f(b)).

        Parameters
        ------------
        x_vals : np.array
            Endpoints with which we compute the area of rectangles
        func : np.ufunc
            The function that x_vals are ran through to compute the height of the func at given x inputs

        Returns
        ------------
        float
            The area of the Riemann approximation
        """
    approx = 0 # creates the approximation
    n = len(x_vals) - 1
    for i in range(n): # iterates for each section
        area = (x_vals[i+1] - x_vals[i])/6 * (func(x_vals[i]) + func(x_vals[i+1]) + 4*(func((x_vals[i] + x_vals[i+1])/2))) # calculates area using simpson
        approx += area
    return approx