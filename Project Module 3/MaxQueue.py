from SLLQueue import SLLQueue
from DLList import DLList
from Interfaces import Queue

class MaxQueue(Queue):
    def __init__(self):
        self.sll = SLLQueue()
        self.dll = DLList()
        # self.n is stored in sll

    # Book object overrides < and >
    def add(self, x: object) -> None:

        self.sll.add(x)

        curr = self.dll.dummy.next
        n = 0

        # find where to add x
        while curr is not self.dll.dummy and not curr.x < x:
            curr = curr.next
            n += 1
        self.dll.add_before(curr, x)
        curr.prev.next = self.dll.dummy
        self.dll.dummy.prev = curr.prev
        self.dll.n = n + 1
        return

        """
        if self.dll.size() == 0:
            self.dll.append(x)
            return

        # dummy.next and dummy,prev need to be changed
        if self.dll.size() == 1:
            if x > self.dll.get(0):
                self.dll.set(0, x)
            else:
                self.dll.append(x)
            return

        # find location to put new element
        # keep track of elements in dll to update it's size
        curr = self.dll.dummy.next
        n = 1
        while curr is not self.dll.dummy and curr.x >= x:
            curr = curr.next
            n += 1

        self.dll.add_before(curr, x)
        # dummy, ?, curr/dummy
        # dummy, ?, new_node, dummy
        # dummy, new_node, dummy
        # dummy, ... new_node, curr, ..., dummy
        # dummy, ... new_node, dummy
        curr.prev.next = self.dll.dummy
        self.dll.dummy.prev = curr.prev
        self.dll.n = n
        """

    def remove(self) -> [int, object]:
        # remove from DLL head if head.x == sll.x
        x = self.sll.remove()
        if x == self.dll.get(0): # get(0) is the head
            self.dll.remove(0)
        return x

    def size(self) -> int:
        return self.sll.n

    def max(self, ) -> object:
        if self.dll.size() == 0:
            print("WARNING: MaxQueue is Empty")
            return None
        return self.dll.get(0)

    def __str__(self):
        return str(self.sll)
