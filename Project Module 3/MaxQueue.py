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
        pass

    def remove(self) -> [int, object]:
        pass

    def size(self) -> int:
        return self.sll.n

    def max(self, ) -> object:
        pass

    def __str__(self):
        return str(self.sll)