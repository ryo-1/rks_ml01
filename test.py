# -*- coding: utf-8 -*-
import rakus_ml_training as rmt
import pandas as pd
import numpy as np
import scaling


def check(W):
    test = rmt.boston.get_test_data()

    for key in test.keys():
        test[key] = scaling.test_zscore(test[key], key)

    test = np.hstack((test ** 2, test))
    test = np.hstack((np.ones((test.shape[0], 1)), test))

    Y_t = test.dot(W)

    return rmt.boston.confirm(pd.DataFrame(Y_t))