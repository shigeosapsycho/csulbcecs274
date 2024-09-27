from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree
from Interfaces import Set

red = 0
black = 1


class RedBlackTree(BinarySearchTree, Set):

    def _new_node(self, x, v):
        u = BinaryTree.Node(x, v)
        u.left = u.right = u.parent = self.nil
        u.color = black
        u.x = x
        u.v = v
        return u

    def __init__(self):
        BinarySearchTree.__init__(self)
        self.nil = self._new_node(None, None)
        self.nil.right = self.nil.left = self.nil.parent = self.nil
        self.r = self.nil

    def push_black(self, u):
        u.color -= 1
        u.left.color += 1
        u.right.color += 1

    def pull_black(self, u):
        u.color += 1
        u.left.color -= 1
        u.right.color -= 1

    def flip_left(self, u):
        self.swap_colours(u, u.right)
        self.rotate_left(u)

    def flip_right(self, u):
        self.swap_colours(u, u.left)
        self.rotate_right(u)

    def swap_colours(self, u, w):
        (u.color, w.color) = (w.color, u.color)

    def add(self, x: object, v: object):
        new_node = self._new_node(x, v)
        if self.r == self.nil:
            self.r = new_node
            new_node.color = black
        else:
            self.add_node(new_node)
        self.add_fixup(new_node)

    def add_fixup(self, u):
        while u != self.r and u.parent.color == red:
            if u.parent == u.parent.parent.left:
                y = u.parent.parent.right
                if y.color == red:
                    u.parent.color = black
                    y.color = black
                    u.parent.parent.color = red
                    u = u.parent.parent
                else:
                    if u == u.parent.right:
                        u = u.parent
                        self.rotate_left(u)
                    u.parent.color = black
                    u.parent.parent.color = red
                    self.rotate_right(u.parent.parent)
            else:
                y = u.parent.parent.left
                if y.color == red:
                    u.parent.color = black
                    y.color = black
                    u.parent.parent.color = red
                    u = u.parent.parent
                else:
                    if u == u.parent.left:
                        u = u.parent
                        self.rotate_right(u)
                    u.parent.color = black
                    u.parent.parent.color = red
                    self.rotate_left(u.parent.parent)
        self.r.color = black

    def remove(self, x):
        node_to_remove = self.find_eq(x)
        if node_to_remove is None:
            return False
        self.remove_node(node_to_remove)
        return True

    def remove_node(self, u: BinaryTree.Node):
        if u.left == self.nil or u.right == self.nil:
            v = u
        else:
            v = self.next_node(u)
        if v.left != self.nil:
            s = v.left
        else:
            s = v.right
        s.parent = v.parent
        if v.parent == self.nil:
            self.r = s
        else:
            if v == v.parent.left:
                v.parent.left = s
            else:
                v.parent.right = s
        if v != u:
            u.x = v.x
        if v.color == black:
            self.remove_fixup(s)

    def remove_fixup(self, u):
        while u != self.r and u.color == black:
            if u == u.parent.left:
                w = u.parent.right
                if w.color == red:
                    w.color = black
                    u.parent.color = red
                    self.rotate_left(u.parent)
                    w = u.parent.right
                if w.left.color == black and w.right.color == black:
                    w.color = red
                    u = u.parent
                else:
                    if w.right.color == black:
                        w.left.color = black
                        w.color = red
                        self.rotate_right(w)
                        w = u.parent.right
                    w.color = u.parent.color
                    u.parent.color = black
                    w.right.color = black
                    self.rotate_left(u.parent)
                    u = self.r
            else:
                w = u.parent.left
                if w.color == red:
                    w.color = black
                    u.parent.color = red
                    self.rotate_right(u.parent)
                    w = u.parent.left
                if w.right.color == black and w.left.color == black:
                    w.color = red
                    u = u.parent
                else:
                    if w.left.color == black:
                        w.right.color = black
                        w.color = red
                        self.rotate_left(w)
                        w = u.parent.left
                    w.color = u.parent.color
                    u.parent.color = black
                    w.left.color = black
                    self.rotate_right(u.parent)
                    u = self.r
        u.color = black

    def rotate_left(self, u: BinaryTree.Node):
        r = u.right
        u.right = r.left
        if r.left != self.nil:
            r.left.parent = u
        r.parent = u.parent
        if u.parent == self.nil:
            self.r = r
        else:
            if u == u.parent.left:
                u.parent.left = r
            else:
                u.parent.right = r
        r.left = u
        u.parent = r

    def rotate_right(self, u: BinaryTree.Node):
        l = u.left
        u.left = l.right
        if l.right != self.nil:
            l.right.parent = u
        l.parent = u.parent
        if u.parent == self.nil:
            self.r = l
        else:
            if u == u.parent.right:
                u.parent.right = l
            else:
                u.parent.left = l
        l.right = u
        u.parent = l