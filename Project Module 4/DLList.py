from timeit import dummy_src_name

from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("") # where is dummy at - the start and end of the list
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def contains(self, x: object) -> bool:
        curr = self.dummy.next
        while curr is not self.dummy:
            if curr.x == x:
                return True
            curr = curr.next
        return False

    # helper method
    def get_node(self, i: int) -> Node:

        if i == self.n:
            return self.dummy # ability to add to the end of the list
        if not 0 <= i < self.n:
            raise IndexError

        curr = self.dummy
        if i < self.n/2:
            for _ in range(i + 1):
                curr = curr.next
        else:
            for _ in range(self.n - i):
                curr = curr.prev
        return curr

    def get(self, i) -> object:
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        self.get_node(i).x = x
        return x

    # helper method, x is the val to add (index is unknown?)
    def add_before(self, w: Node, x: object) -> Node:
        new_node = self.Node(x)

        # w.prev -> w to
        # w.prev -> new_node -> w
        new_node.prev, new_node.next = w.prev, w
        w.prev.next, w.prev = new_node, new_node
        self.n += 1
        return new_node

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:  raise IndexError()
        self.add_before(self.get_node(i), x)

    # helper method, w is the node to be removed (index is unknown?)
    def _remove(self, w: Node) -> object:
        x = w.x
        # before -> w -> after
        # before -> after
        w.next.prev = w.prev
        w.prev.next = w.next
        self.n -= 1
        return x

    def remove(self, i: int) -> object:
        if i < 0 or i >= self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    # case and punctuation do not matter
    def isPalindrome(self) -> bool:
        while self.size() > 1: # size() 0 and 1 are always palindromes
            front = self.remove(0)
            back = self.remove(self.size() -1)
            if front != back: return False
        return True

    def reverse(self) -> None:
        # reverses from self.dummy to self.dummy
        curr = self.dummy
        for i in range(self.n + 1):
            old_next = curr.next
            curr.next = curr.prev
            curr.prev = old_next
            curr = curr.next

    # clear() - clears the whole dll and returns the list equivalent
    """
    def clear(self) -> list:
        if self.n == 0:
            raise IndexError("List is empty.")
        data = list()
        for i in range(self.n):
            data.append(self.get_node(i).x)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        return data
    """

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            # note: added "and u is not self.dummy"
            if u is not None and u is not self.dummy:
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
