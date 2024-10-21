import numpy as np
from Interfaces import List
# from project_template.BinaryHeap import right


class ArrayList(List):
    """
        ArrayList: Implementation of a List interface using Arrays.
    """

    def __init__(self):
        """
        __init__: Initialize the state (array, n and j).
        """
        self.n = 0
        self.j = 0 # index of first element in the array
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        """
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        """
        return np.zeros(n, object)

    def resize(self):
        """
        resize: Create a new array and copy the old values.
        """
        b = self.new_array(max(1, 2 * self.n))
        # self.j + self.n represents the index without looping
        for i in range(self.n):
            # loop this index to the different array sizes
            b[i] = self.a[(self.j + i) % len(self.a)]
        self.j = 0
        self.a = b

    def get(self, i: int) -> object:
        """
        get: returns the element at position i
        Inputs:
            i: Index that is integer non-negative and at most n
        """
        if not 0 <= i < self.n:
            raise IndexError()
        return self.a[(self.j + i) % len(self.a)]


    def set(self, i: int, x: object) -> object:
        """
        set: Set the value x at the index i.
        Inputs:
            i: Index that is integer non-negative and at most n
            x: Object type, i.e., any object
        """
        if not 0 <= i < self.n:
            raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y


    def append(self, x: object):
        self.add(self.n, x)

    def add(self, i: int, x: object):
        """
            add: shift one position all the items j>=i, insert an element
            at position i of the list and increment the number of elements
            in the list
            Inputs:
                i: Index that is integer non-negative and at most n
                x: Object type, i.e., any object
        """
        if not 0 <= i <= self.n:
            raise IndexError()

        if self.n == len(self.a):
            self.resize()

        # shift left side
        if i < self.n/2:
            # does not move elem at i, places x one left of i
            # shift going left to right to one before i
            for k in range(0, i):
                left_index = (self.j + k - 1) % len(self.a)
                right_index = (self.j + k) % len(self.a)
                self.a[left_index] = self.a[right_index]
            # move j one left
            self.j = (self.j - 1) % len(self.a)

        # shift right side
        else:
            # moves elem at i to the right, places x at i
            # shift going right to left to i
            for k in range(self.n -1, i-1, -1):
                left_index = (self.j + k) % len(self.a)
                right_index = (self.j + k + 1) % len(self.a)
                self.a[right_index] = self.a[left_index]

        self.a[(self.j + i) % len(self.a)] = x
        self.n += 1


    def remove(self, i: int) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()

        y = self.a[(self.j + i) % len(self.a)]
        # on both shifts, the first loop brings in the outer element
        # shift left side
        if i < self.n / 2:
            # shift going right (in) to left (out)
            for k in range(i, 0, -1):
                left_index = (self.j + k - 1) % len(self.a)
                right_index = (self.j + k) % len(self.a)
                self.a[right_index] = self.a[left_index]
            # move j one right
            self.j = (self.j + 1) % len(self.a)
            # set far left elem to empty value (0)
            self.a[(self.j - 1) % len(self.a)] = 0

        # shift right side
        else:
            # go left to right
            for k in range(i, self.n -1):
                left_index = (self.j + k) % len(self.a)
                right_index = (self.j + k + 1) % len(self.a)
                self.a[left_index] = self.a[right_index]
            # set far right elem to empty value (0)
            self.a[(self.j + self.n -1) % len(self.a)] = 0

        self.n -= 1
        if len(self.a) > 3*self.n:
            self.resize()

        return y

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
