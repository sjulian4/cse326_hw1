
# equation: f(x) = e^{-x^4}-x^3+cos(1-x^2)
# data: https://docs.google.com/spreadsheets/d/1ISUL8f31Oi0aGR5STT-P3AiG6PJPRuMBblmrMWydlx0/edit?usp=sharing
import numpy as np

def f(x):
    return np.exp(-x**4) - x**3 - np.cos(1 - x**2)

def df(x):
    return -4*x**3 * np.exp(-x**4) - 3*x**2 + 2*x*np.sin(1 - x**2)

x_true = 0.54075

def main():

    # run bisection method with [-1,1]
    x_low = -1.0
    x_high = 1.0
    iters0 = int(1.0e4)

    for i in range(iters0):
        x_mid = (x_low + x_high) / 2.0
        if abs(f(x_mid)) < 5.0e-5:
            print("Bisection method: approximate root is " + str(x_mid) + ". Iterations: " + str(i+1) + ".\nRelative error: " + str(100.0 * abs(x_mid - x_true) / x_true) + "%.")
            break
        if(f(x_high) * f(x_mid) < 0.0):
            x_low = x_mid
        elif f(x_low) * f(x_mid) < 0.0:
            x_high = x_mid


    # run Newton's method with initial guess x0 =0.1111

    iters1 = int(1.0e3)
    x_0 = 0.1111
    for i in range(iters1):
        x_0 = x_0 - f(x_0) / df(x_0)
        if abs(f(x_0)) < 5.0e-5:
            print("Newton's method: approximate root is " + str(x_0) + ". Iterations: " + str(i+1) + ".\nRelative error: " + str(100.0 * abs(x_0 - x_true) / x_true) + "%.")
            break

    # run secand method with 
    iters2 = int(1.0e3)
    x_0 = -1.0
    x_1 = 1.0
    for i in range(iters2):
        x_2 = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))
        x_0 = x_1
        x_1 = x_2
        if abs(f(x_1)) < 5.0e-5:
            print("Secant method: approximate root is " + str(x_1) + ". Iterations: " + str(i+1) + ".\nRelative error: " + str(100.0 * abs(x_1 - x_true) / x_true) + "%.")
            break

    
    # run monte carlo method with [0.3,0.7]
    np.random.seed(2)

    guess_arr = np.random.uniform(0.3, 0.7, int(1.0e4))
    for i in range(guess_arr.size):
        if abs(f(guess_arr[i])) < 5.0e-5:
            print("Monte Carlo method: approximate root is " + str(guess_arr[i]) + "Iterations: " + str(i+1) + ".\nRelative error: " + str(100.0 * abs(guess_arr[i] - x_true) / x_true) + "%.")
            break



if __name__ == "__main__":
       main()
