from SLLQueue import SLLQueue
from DLList import DLList
from Interfaces import Queue


class MaxQueue(Queue):
    def __init__(self):
        self.sll = SLLQueue()
        self.dll = DLList()
        # self.n is stored in sll

    # note: Book object has dunder methods that overrides < and >
    def add(self, x: object) -> None:
        self.sll.add(x)

        while self.dll.size() > 0 and x > self.dll.get(self.dll.size() - 1):
            self.dll.remove(self.dll.size() - 1)
        self.dll.add(self.dll.size(), x)

    def remove(self) -> object:
        if self.size() == 0:
            raise IndexError()
        
        removed_item = self.sll.remove()

        if removed_item == self.dll.get(0):
            self.dll.remove(0)

        return removed_item

    def size(self) -> int:
        return self.sll.n
    
    def max(self) -> object:
        if self.size() == 0:
            raise IndexError()
        return self.dll.get(0)

    def __str__(self):
        return str(self.sll)