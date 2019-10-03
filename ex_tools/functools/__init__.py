from functools import *
from .x_object import X, F
from .pipe import Pipe


def tee(value):
    print('tee:', value)
    return value
