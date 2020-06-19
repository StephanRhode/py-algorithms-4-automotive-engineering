import numpy as np
import matplotlib.pyplot as plt


def plot_data(X_train, y_train, X_test, y_test):
    plt.figure(figsize=(14, 8))

    m = X_train.shape[0]
    k_val = X_test.shape[0]

    ax1 = plt.subplot(311)
    plt.plot(np.arange(0, m), X_train[:, 0], 'k')
    plt.plot(np.arange(m, m+k_val), X_test[:, 0], 'r')
    ax1.set_ylabel('velocity')

    ax2 = plt.subplot(312)
    plt.plot(np.arange(0, m), X_train[:, 1], 'k')
    plt.plot(np.arange(m, m+k_val), X_test[:, 1], 'r')
    ax2.set_ylabel('acceleration')

    ax3 = plt.subplot(313)
    plt.plot(np.arange(0, m), y_train, 'k')
    plt.plot(np.arange(m, m+k_val), y_test, 'r')
    ax3.set_ylabel('power')