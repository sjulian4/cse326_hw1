
# equation: f(x) = e^{-x^4}-x^3+cos(1-x^2)
import numpy as np
def f(x):
    return np.exp(-x**4) - x**3 + np.cos(1 - x**2)

# Bisection Method
def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function has the same signs at the endpoints a and b.")
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Newton's Method
def newtons_method(func, dfunc, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = dfunc(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x = x - fx / dfx
    return x

# Secant Method
def secant_method(func, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        f_x0 = func(x0)
        f_x1 = func(x1)
        if abs(f_x1) < tol:
            return x1
        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero in secant method.")
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

# Monte Carlo Method
def monte_carlo_method(func, lower_bound, upper_bound, num_samples=100000):
    samples = np.random.uniform(lower_bound, upper_bound, num_samples)
    func_values = func(samples)
    min_index = np.argmin(np.abs(func_values))
    return samples[min_index]

def main():
    # Define the derivative of f for Newton's method

    # Bisection Method
    root_bisection = bisection_method(f, -1, 1)
    print(f"Bisection Method Root: {root_bisection}")

    # Newton's Method
    root_newton = newtons_method(f, df, x0=0.1111)
    print(f"Newton's Method Root: {root_newton}")

    # Secant Method
    root_secant = secant_method(f, x0=-1, x1=1)
    print(f"Secant Method Root: {root_secant}")

    # Monte Carlo Method
    root_monte_carlo = monte_carlo_method(f, 0.3, 0.7)
    print(f"Monte Carlo Method Root: {root_monte_carlo}")