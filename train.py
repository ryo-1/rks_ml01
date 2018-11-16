import rakus_ml_training as rmt
import pandas as pd
import numpy as np
import scaling


def normal_equation():
    train = rmt.boston.get_train_data()
    X = train.drop('TARGET', axis=1)
    Y = pd.DataFrame(train.get('TARGET'))

    for key in X.keys():
        X[key] = scaling.zscore(X[key], key)

    X = np.hstack((X ** 2, X))
    X = np.hstack((np.ones((X.shape[0], 1)), X))

    return np.array(np.dot(np.linalg.inv(X.T.dot(X)), X.T.dot(Y)))
