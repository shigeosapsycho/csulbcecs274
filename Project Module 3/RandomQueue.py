import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        if self.n == 0:
            raise IndexError()

        rand_n = random.randint(0, self.n - 1)
        rand_index = (self.j + rand_n) % len(self.a)
        res = self.a[rand_index]
        self.a[rand_index] = self.a[self.j]

        # old data will be overwritten but
        # in init "0" represents empty
        self.a[self.j] = 0

        self.j += 1
        self.n -= 1
        if len(self.a) > 3 * self.n:
            self.resize()
        return res
