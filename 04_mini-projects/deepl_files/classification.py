import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from matplotlib.image import imread


# %% Data

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def getdata(folder):
    files = glob.glob(folder + '/*')

    labels = [os.path.basename(file).split('_')[0] for file in files]
    labels = np.array(labels, dtype=np.int)[:, np.newaxis]
    cases = np.unique(labels)
    labels = np.array(
        [[i for i in range(len(cases)) if label == cases[i]] for label in labels])

    images = np.array([imread(file) for file in files])

    print(images.shape)
    print(labels.shape)

    return images, labels


IMAGES, LABELS = getdata(folder='data')

for image in IMAGES[9:12]:
    plt.figure()
    plt.imshow(image)
    plt.show()

folder_t = 'data_test'
images_t, labels_t = getdata(folder_t)

# %% Model

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=IMAGES[0].shape),
    tf.keras.layers.Dense(64, 'relu'),
    tf.keras.layers.Dense(16, 'relu'),
    # tf.keras.layers.Dense(len(cases)),
    tf.keras.layers.Dense(len(np.unique(LABELS)), 'softmax')
])

model.compile(
    optimizer='adam',
    # loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

# %% Predict

labels_m = model.predict(IMAGES[9:12])
print(LABELS[9:12])
print(labels_m)
print(np.argmax(labels_m, axis=1)[:, np.newaxis])

# %% Train

model.fit(IMAGES, LABELS, epochs=5, verbose=2, batch_size=len(IMAGES))

# %% Predict on training data

labels_m = model.predict(IMAGES[9:12])
print(LABELS[9:12])
print(labels_m)
print(np.argmax(labels_m, axis=1)[:, np.newaxis])

model.evaluate(IMAGES, LABELS, verbose=2)

# %% Predict on test data

model.evaluate(images_t, labels_t, verbose=2)
