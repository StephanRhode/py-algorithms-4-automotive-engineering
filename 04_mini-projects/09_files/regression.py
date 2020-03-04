import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from mpl_toolkits import mplot3d

# %% Data

# Input and outplut
xs = np.array([[x1, x2] for x1 in np.linspace(0, np.pi, 20) for x2 in
               np.linspace(0, 2 * np.pi, 20)])
ys = 3 * np.sin(np.sum(xs, axis=1, keepdims=True)) + 10
print(xs.shape)
print(ys.shape)

# Rescale with mean and standard deviation for better usage of activation functions
mu = np.mean(xs, axis=0)
sig = np.std(xs, axis=0)
xs = (xs - mu) / sig

# %% Model

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, input_shape=[2], activation='relu'),  # 16x2 + 16 = 48
    tf.keras.layers.Dense(8, activation='relu'),  # 8x16 + 8 = 136
    tf.keras.layers.Dense(1)  # 1x8 + 1 = 9
])

# Model summary
model.summary()

# Setup
model.compile(loss='mse', optimizer='adam')

# Plot initial predictions
ys_m = model.predict(xs)
plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xs[:, 0], xs[:, 1], ys)
ax.scatter(xs[:, 0], xs[:, 1], ys_m)

# %% Train

model.fit(xs, ys, epochs=500, verbose=2)

# %% Plot after training

ys_m = model.predict(xs)
plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xs[:, 0], xs[:, 1], ys)
ax.scatter(xs[:, 0], xs[:, 1], ys_m)

plt.show()
