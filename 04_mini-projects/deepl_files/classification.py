import glob
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from matplotlib.image import imread
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# For image from url
from PIL import Image
import requests
from io import BytesIO

# %% Data

def getdata(folder):
    files = glob.glob(folder + '/*')
    
    images = np.array([imread(file) for file in files])

    labels = np.array([
        os.path.basename(file).split('_')[0] for file in files
        ], dtype=np.int)
    
    return images, labels

# Images and labels
images, labels = getdata('data')
print(labels)
C = len(np.unique(labels))
print('Number of classes: %i' % C)
for i in [0,10,20]:
    plt.figure()
    plt.imshow(images[i])
    plt.show()
    
# %% Transform to probabilities

# Encode labels to integers corresponding to classes
encoder = LabelEncoder()
labels_int = encoder.fit_transform(labels)
print(labels_int)

# One-hot enconding corresponding to "probabilities"
encoder_onehot = OneHotEncoder(sparse=False)
y = encoder_onehot.fit_transform(labels_int.reshape([-1,1]))
print(y)

# Decode
labels2 = encoder.inverse_transform(np.argmax(y,axis=1))
print('Check decoding')
print(labels)
print(labels2)

# %% Test data

images_test, labels_test = getdata('data_test')
y_test = encoder_onehot.fit_transform(encoder.fit_transform(labels_test).reshape([-1,1]))

# %% Model

print('Shape of input image data')
print(images[0].shape)

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=images[0].shape),
    tf.keras.layers.Dense(64, 'relu'),
    tf.keras.layers.Dense(16, 'relu'),
    tf.keras.layers.Dense(C, 'softmax')
])
model.summary()
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy()
    ,optimizer = 'adam'
    ,metrics=['accuracy']
    )

#%% Evaluate accuracy

# Evaluate
y_m = model.predict(images)
print(y[:3])
print(y_m[:3])
print(np.sum(y_m,axis=1)[:3])

# Compute accuracy
labels_int_m = np.argmax(y_m,axis=1)
print('\nPredicted labels_int at model initialization')
print(labels_int_m)
print('labels_int')
print(labels_int)
correct_events = np.sum(labels_int == labels_int_m)
acc = correct_events/len(labels)
print('Correct events: %i' % correct_events)
print('Accuracy: %.2f' % acc)

# Evaluate
model.evaluate(images,y)

# %% Train

model.fit(images, y, epochs=10, verbose=2)

# %% Evaluate accuracy after training

model.evaluate(images,y)
model.evaluate(images_test,y_test)

# %% Try to predict for a street sign

# Get image
url = 'https://w.grube.de/media/image/7b/5f/63/art_78-101_1.jpg'
response = requests.get(url)
sign = Image.open(BytesIO(response.content))
print(sign)

# Plot
plt.figure()
plt.imshow(sign)
plt.show()

# Resize
sign = sign.resize([20,20])
plt.figure()
plt.imshow(sign)
plt.show()

# Careful: imported image values != as training images 
sign = np.array(sign)
print('\nValues at pixel(0,0)')
print(sign[0,0,:])

# Transform to range [0,1]
sign = sign/255
print('\nValues at pixel(0,0)')
print(sign[0,0,:])

# Predict with trained model
y_sign = model.predict(np.array([sign]))
print('\nPredicted probabilities')
print(y_sign)
print(encoder.inverse_transform(np.argmax(y_sign,axis=1)))


