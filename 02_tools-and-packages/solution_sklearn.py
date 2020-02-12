import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


digits = datasets.load_digits()
digits_X = n_samples = digits.images.reshape((len(digits.images), -1))
digits_X_train, digits_X_test, digits_y_train, digits_y_test = \
    train_test_split(digits_X, digits.target, test_size=0.3, shuffle=True)

clf = MLPClassifier(hidden_layer_sizes=(5), random_state=1)
clf.fit(digits_X_train, digits_y_train)

print("Classification accuracy report\n",
    metrics.classification_report(digits_y_test, clf.predict(digits_X_test))
)

# present neural networks's accuracy in a confusion matrix
metrics.plot_confusion_matrix(clf, digits_X_test, digits_y_test)
plt.show()
