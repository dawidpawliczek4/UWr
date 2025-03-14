import numpy as np

def calculate_pi(precision, dtype):
    pi_approx = np.zeros(1, dtype=dtype)
    k = 0
    term = np.ones(1, dtype=dtype)
    
    while np.abs(term) > precision:
        term = 4*((-1) ** k) / (2 * k + 1)
        pi_approx += np.array([term], dtype=dtype)
        k += 1
        
    return pi_approx[0], k

precision = 1e-6

pi_float32, terms_float32 = calculate_pi(precision, np.float32)

pi_float64, terms_float64 = calculate_pi(precision, np.float64)

print(pi_float32, terms_float32, pi_float64, terms_float64)