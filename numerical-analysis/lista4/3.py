import numpy as np

def f(x):
    return x - 0.49

a0 = 0
b0 = 1

def bisection_method(a0, b0, steps):
    errors = []
    estimates = []
    a, b = a0, b0

    for n in range(steps):
        # Calculate the midpoint
        m = (a + b) / 2

        # Determine the new interval [a_n+1, b_n+1]
        if f(m) < 0:
            a = m
        else:
            b = m

        # Calculate the error |e_n|
        error = abs(0.49 - m)
        estimate = (b0 - a0) / (2 ** (n + 1))

        # Store the errors and estimates
        errors.append(error)
        estimates.append(estimate)

    return errors, estimates

errors, estimates = bisection_method(a0, b0, 5)
print(errors)
print(estimates)