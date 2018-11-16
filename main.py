# -*- coding: utf-8 -*-
import train
import test

if __name__ == '__main__':
    W = train.normal_equation()
    print(test.check(W))