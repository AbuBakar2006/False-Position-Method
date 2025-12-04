# False Position Method to find root of a function

# Importing necessary libraries
import numpy as np
import sys


def f(x): return np.exp(x)-np.sin(x)  # Function definition
# Function can be changed as per requirement


a = float(input("Enter Num1: "))  # Taking point a from user
b = float(input("Enter Num2: "))  # Taking point b from user
tol = 1e-7  # Tolerance
n = 100  # Maximum number of iterations
i = 1  # Iteration counter
fa = f(a)
fb = f(b)

if np.sign(fa) == np.sign(fb):
    print("No root exists in the given interval")
    sys.exit()
while i <= n:
    c = (a*fa - b*fb)/(fa - fb)  # False Position Formula
    fc = f(c)  # Function value at c
    if abs(fc) < tol:
        # Root found
        sys.exit(print(f"Root found at x = {c} after {i} iterations"))
    elif np.sign(fc) == np.sig1n(fa):
        a = c
        fa = fc
    else:
        b = c
        fb = fc
    i += 1

if i > n:
    print("Maximum iterations reached without finding root")
