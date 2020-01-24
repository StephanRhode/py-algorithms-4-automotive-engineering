import random
import matplotlib.pyplot as plt

x = [i for i in range(0, 1500)]
y = [random.gauss(mu=0, sigma=1) for i in range(0, 1500)]

plt.hist(y, bins=40)
plt.xlabel('Data')
plt.ylabel('Probability density')
plt.title(r'Histogram of Gaussian dist: $\mu=0$, $\sigma=1$')
plt.show()