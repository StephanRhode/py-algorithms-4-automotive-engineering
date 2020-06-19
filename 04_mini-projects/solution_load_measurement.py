def load_measurement(file, test_size=200):
    import scipy.io
    import os

    def find_mat(filename):
        if os.path.isfile(filename):
            curr_file = filename
        else:
            curr_file = '04_mini-projects/' + filename
        return curr_file

    dat = scipy.io.loadmat(find_mat('dat1.mat'))
    m = dat['A'].shape[0]
    X_train = dat['A'][0:m-test_size]
    y_train = dat['B'][0:m-test_size]
    X_test = dat['A'][-test_size:]
    y_test = dat['B'][-test_size:]
    return X_train, y_train, X_test, y_test