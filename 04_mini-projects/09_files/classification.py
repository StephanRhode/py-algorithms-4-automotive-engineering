import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import glob

#%% Data

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def getdata(folder):
    files = glob.glob(folder+'/*')
    
    labels = [file.split('\\')[-1].split('_')[0] for file in files]
    labels = np.array(labels,dtype=np.int)[:,np.newaxis]
    cases = np.unique(labels)
    labels = np.array([[i for i in range(len(cases)) if label==cases[i]] for label in labels])
    
    images = np.array([imread(file) for file in files])
    # images = np.array([rgb2gray(imread(file)) for file in files])
    
    print(images.shape)
    print(labels.shape)
    
    return images, labels

folder = 'data'
images, labels = getdata(folder)

for image in images[9:12]:
    plt.figure()
    plt.imshow(image)
    plt.show()
    
folder_t = 'data_test'
images_t, labels_t = getdata(folder_t)
    
#%% Model
    
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=images[0].shape)
    ,tf.keras.layers.Dense(64,'relu')
    ,tf.keras.layers.Dense(16,'relu')
    # ,tf.keras.layers.Dense(len(cases))
    ,tf.keras.layers.Dense(len(np.unique(labels)),'softmax')
    ])

model.compile(
    optimizer='adam'
    # ,loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    ,loss=tf.keras.losses.SparseCategoricalCrossentropy()
    ,metrics=['accuracy']
    )

#%% Predict

labels_m = model.predict(images[9:12])
print(labels[9:12])
print(labels_m)
print(np.argmax(labels_m,axis=1)[:,np.newaxis])

#%% Train

model.fit(
    images
    ,labels
    ,epochs=5
    ,verbose=2
    ,batch_size=len(images)
    )

#%% Predict on training data

labels_m = model.predict(images[9:12])
print(labels[9:12])
print(labels_m)
print(np.argmax(labels_m,axis=1)[:,np.newaxis])

model.evaluate(
    images
    ,labels
    ,verbose=2
    )

#%% Predict on test data

model.evaluate(
    images_t
    ,labels_t
    ,verbose=2
    )