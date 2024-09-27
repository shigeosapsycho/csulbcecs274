from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        BinaryTree.__init__(self)
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
        
    def find_last(self, x: object) -> BinaryTree.Node:
        w = self.r
        prev = self.nil
        while w != self.nil:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev

    def add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        if p == self.nil:
            self.r = u
        elif u.x < p.x:
            p.left = u
        else:
            p.right = u
        u.parent = p
        self.n += 1
        return True

    def find_eq(self, x: object) -> object:
        u = self.r
        while u != self.nil:
            if x < u.x:
                u = u.left
            elif x > u.x:
                u = u.right
            else:
                return u.v
        return None

    def find(self, x: object) -> object:
        u = self.find_last(x)
        if u != self.nil and u.x == x:
            return u.v
        return None

    def splice(self, u: BinaryTree.Node):
        if u.left != self.nil:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            s.parent = self.nil
        else:
            if u == u.parent.left:
                u.parent.left = s
            else:
                u.parent.right = s
            s.parent = u.parent

    def remove(self, x: object) -> bool:
        u = self.find_last(x)
        if u == self.nil or u.x != x:
            return False
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = self.next_node(u)
            u.x = w.x
            u.v = w.v
            self.splice(w)
        self.n -= 1
        return True
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


            
