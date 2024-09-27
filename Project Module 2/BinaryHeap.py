import numpy as np
from Interfaces import Queue



def left(i: int):
    return 2 * i + 1

def right(i: int):
    return 2 * i + 2

def parent(i: int):
    return (i - 1) // 2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)

    def resize(self):
        new_capacity = max(1, 2 * self.n)  # Step 1: Create a new array of size 2 * n
        b = self.new_array(new_capacity)   # Create a new array with the new capacity
        for i in range(self.n):            # Step 2: Copy elements from the old array to the new array
            b[i] = self.a[i]
        self.a = b                         # Step 3: Set the new array as the heap's array

    def add(self, x: object):
        if len(self.a) == self.n:
            self.resize()
        self.a[self.n] = x
        self.n += 1
        self.bubble_up(self.n - 1)

    def bubble_up(self, i):
        p = parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = parent(i)

    def remove(self):
        if self.n == 0:
            raise IndexError("remove from empty heap")
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self.trickle_down(0)
        if len(self.a) >= 3 * self.n:
            self.resize()
        return x

    def trickle_down(self, i):
        while left(i) < self.n:
            smallest = left(i)
            if right(i) < self.n and self.a[right(i)] < self.a[smallest]:
                smallest = right(i)
            if self.a[i] <= self.a[smallest]:
                break
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            i = smallest

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"


