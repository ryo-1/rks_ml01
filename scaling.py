# -*- coding: utf-8 -*-
import numpy as np


xmean = {}
xstd = {}


def min_max_scaling(x):
    return (x - x.min()) / (x.max() - x.min())


def zscore(x, key):
    global xmean
    global xstd

    xmean[key] = x.mean()
    xstd[key] = np.std(x)
    return (x-xmean[key])/xstd[key]