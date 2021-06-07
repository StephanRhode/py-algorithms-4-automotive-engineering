import matplotlib.pyplot as plt
import numpy as np

n = 2
m = 1000


def predict(a_mat, x_vec):
    """You need to care about single and multidimensional arrays."""
    return (a_mat @ x_vec).flatten()


# create sin and cos input data
time = np.linspace(0, 10, m)
a = np.vstack((np.sin(time), np.cos(time))).T

# choose a parameter vector
x = np.array([[3.], [-8.]])
print("True params", x.flatten())

# create noise
noise = np.random.randn(m) * 0.1

# predict model with additive noise
b = predict(a, x) + noise

# solve least squares estimate
ata = a.T @ a
atb = a.T @ b
x_hat = np.linalg.solve(a=ata, b=atb)

print("Estimated params", x_hat)

plt.plot(b, 'k.')
plt.title("A linear regression task")
plt.plot(predict(a, x_hat), 'r:')
plt.legend(["Noisy data", "Least squares estimate"])
plt.show()
