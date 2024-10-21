from wsgiref.validate import header_re

from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def push(self, x: object) -> None:
        # add at the head
        new_node = self.Node(x)
        if self.n == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        """
        new_node = self.Node(x)
        old_head = self.head
        self.head = new_node
        self.head.next = self.head
        if self.n == 0:
            self.tail = new_node
        """
        self.n += 1

    def pop(self) -> object:
        # remove from the head
        if self.n == 0:
            raise IndexError

        x = self.head.x
        if self.n == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self.n -= 1
        return x


    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
