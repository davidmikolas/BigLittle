import numpy as np

class A(object):
    def __init__(self, x):
        self.x = x
    def sqrtx(self):
        if self.x >= 0:
            y = np.sqrt(self.x)
        else:
            y = 'nope!'
        return y
