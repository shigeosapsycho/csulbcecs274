from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        index = self.hash(key)  # Hash the key to find the bucket
        for node in self.t[index]:  # Check within the appropriate bucket
            if node.key == key:
                return node.value
        return None

    def add(self, key: object, value: object):
        if self.find(key) is not None:
            self.remove(key)
        if self.n + 1 > len(self.t):
            self.resize()
        index = self.hash(key)
        self.t[index].append(self.Node(key, value))  # Add the key-value pair in the appropriate bucket
        self.n += 1
        
    def remove(self, key: int) -> object:
        index = self.hash(key)
        for i, node in enumerate(self.t[index]):
            if node.key == key:
                value = node.value
                del self.t[index][i]
                self.n -= 1
                if 3 * self.n < len(self.t):
                    self.resize()
                return value
        return None

    def resize(self):
        new_size = max(2, 2 * self.n)
        old_t = self.t
        self.t = self.alloc_table(new_size)
        self.n = 0
        for chain in old_t:
            for node in chain:
                self.add(node.key, node.value)

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
