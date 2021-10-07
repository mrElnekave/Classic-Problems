# A binary search tree built in my CS Capstone class.
import Randp


class BST:

    def __init__(self, datum):
        self.datum = datum
        self.right = False
        self.left = False

    def get_datum(self):
        return self.datum

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def depth(self):
        depth = 1
        rdepth = 0
        ldepth = 0
        if self.right:
            rdepth = self.right.depth()
        if self.left:
            ldepth = self.left.depth()
        depth += max(rdepth, ldepth)
        return depth

    def insert(self, datum):
        if datum > self.datum:
            if not self.right:
                self.right = BST(datum)
            else:
                self.right.insert(datum)
        if datum < self.datum:
            if not self.left:
                self.left = BST(datum)
            else:
                self.left.insert(datum)

    def delete(self, datum):
        if datum == self.datum:
            print("cannot delete root node")
        if datum > self.datum:
            if self.right:
                if self.right.get_datum() == datum:
                    self.right = False
                else:
                    self.right.delete(datum)
        if datum < self.datum:
            if self.left:
                if self.left.get_datum() == datum:
                    self.left = False
                else:
                    self.left.delete(datum)

    def getTree(self):
        string = ''
        if self.left:
            string = string + self.left.getTree()
        string += " "
        string += str(self.datum)
        string += " "
        if self.right:
            string += self.right.getTree()
        return string

    # def __contains__(self, item):
    #     return item in self.__repr__()

    def print(self):
        depth = self.depth()
        levels = [[] for i in range(depth-1)]

        def add_level(root, level):
            if not root:
                levels[i-1].append(0)
            elif level == 1:
                levels[i-1].append(root.datum)
            elif level > 1:
                add_level(root.left, level - 1)
                add_level(root.right, level - 1)

        for i in range(depth):
            add_level(self, i)
        for i in range(depth-1):
            print(levels[i])


def basictree():
    r = Randp(1000)
    tree = BST(r.next_int())
    print(tree.datum)
    for i in range(r.numsLeft):
        tree.insert(r.next_int())

    print(tree.getTree())
    print(tree.depth())


def ten_tree():
    r = Randp(30)
    tree = BST(r.next_int())
    for i in range(r.numsLeft):
        tree.insert(r.next_int())
    print(tree.depth())
    tree.print()


ten_tree()


def avg_tree(accuracy):
    depthlot = 0
    for i in range(accuracy):
        r = Randp(1000)
        tree = BST(r.next_int())
        for i in range(r.numsLeft):
            tree.insert(r.next_int())

        depthlot += tree.depth()
    return depthlot/accuracy


# print(avg_tree(10000))
