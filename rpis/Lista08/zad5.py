import numpy as np

data = np.loadtxt('z0805.csv', delimiter=',')

lambda_hat = data.mean()

print(f"Estymator największej wiarygodności λ̂ = {lambda_hat:.4f}")