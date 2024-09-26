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
        if self.size() == 0:
            raise IndexError("remove from empty queue")
        
        index = random.randint(0, self.size() - 1)
        actual_index = (self.j + index) % len(self.a)
        last_index = (self.j + self.n - 1) % len(self.a)
        temp = self.a[actual_index]
        self.a[actual_index] = self.a[last_index]
        self.a[last_index] = None
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return temp
