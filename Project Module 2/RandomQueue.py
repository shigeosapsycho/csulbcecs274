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
        super().remove()
        if self.size() > 0:
            index = random.randint(0, self.size()-1)
            temp = self.a[index]
            self.a[index] = self.a[self.size()-1]
            self.a[self.size()-1] = temp
        return temp