import ArrayQueue

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u: Node) -> int:
        depth = 0
        while u != self.r:
            u = u.parent
            depth += 1
        return depth

    def _size(self, u: Node) -> int:
        if u == self.nil:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def _height(self, u: Node) -> int:
        if u == self.nil:
            return -1
        return 1 + max(self._height(u.left), self._height(u.right))

    def traverse(self, u: Node):
        if u == self.nil:
            return
        self.traverse(u.left)
        print(u.x, end=" ")
        self.traverse(u.right)

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        q.add(self.r)
        while q.size() > 0:
            u = q.remove()
            if u != self.nil:
                print(u.x, end=" ")
                q.add(u.left)
                q.add(u.right)
            
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def in_order(self, u : Node, l : list) :       
        # todo
        pass 

    def __str__(self):
        l = []
        self.in_order(self.r, l)
        return ', '.join(map(str, l))