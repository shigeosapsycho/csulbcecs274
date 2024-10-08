from Interfaces import List
import numpy as np
import re

class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # todo
        if i < 0 or i > self.n: # precondition
            return None
        if i < self.n // 2:
            u = self.dummy.next # head, i = 0
            for j in range(i):
                u = u.next
        else:
            u = self.dummy
            for j in range(self.n, i, -1):
                u = u.prev
        return u # i-th node
    # Time Complexity: O(1) + min{i, n-i}

    def get(self, i) -> object:
        # todo
        if i < 0 or i >= self.n:
            raise Exception()
        return self.get_node(i).x # Return the i-th node
    # Time Complexity: O(1 + min{i, n-i})
        
    def set(self, i: int, x: object) -> object:
        # todo
        if i < 0 or i >= self.n:
            raise Exception()
        u = self.get_node(i) # i-th node
        y = u.x # Data from the i-th node
        u.x = x # Updating/Overwriting Data
        return y
    # Time Complexity: O(1 + min{i, n-i})

    def add_before(self, w: Node, x: object) -> Node:
        # todo
        if w is None:
            raise Exception()
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1
        # Time Complexity: O(1)

    def add(self, i: int, x: object):
        # todo
        if i < 0 or i > self.n: # Precondition
            raise Exception()
        return self.add_before(self.get_node(i), x) # O(1 + min{i, n-i})
    # Time complexity: O(1 + min{i, n-i})

    def _remove(self, i: int):
        # todo
        if i < 0 or i >= self.n:
            raise IndexError()
        w = self.get_node(i)
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x
    # Time Complexity: O(1 + min{i, n-i})

    def remove(self, i: int):
        if i < 0 or i > self.n:  raise IndexError()
        return self._remove(i)

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        s = "".join([str(self.get(i)) for i in range(self.n)])
        
        cleaned_string = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        
        return cleaned_string == cleaned_string[::-1]
    # Time Complexity: O(n)

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x

    def reverse(self):
        current = self.dummy
        for i in range(self.n + 1):
            current.next, current.prev = current.prev, current.next
            current = current.prev