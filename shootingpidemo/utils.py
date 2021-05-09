import numpy as np


class Random2dPoint:
    def __init__(self):
        self.x = None
        self.y = None
        self.pick_random_point()

    def pick_random_point(self):
        self.x, self.y = np.random.rand(2)
