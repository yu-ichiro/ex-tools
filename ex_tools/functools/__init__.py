from functools import *
from .x_object import X, F


def tee(value):
    print('tee:', value)
    return value
