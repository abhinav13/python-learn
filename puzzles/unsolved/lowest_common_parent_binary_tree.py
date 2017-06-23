import sys

class Node():

    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        self.visited = None

    def __str__(self):
        return str(self.cargo)

    def addleftChild(self, lchild):
        self.left = lchild

    def addrightChild(self, rchild):
        self.right = rchild

    def __getitem__(self, item):
        return self


def printTree(node):

    if(node is None):
        return
    if(node.visited is not True):
        printTree(node.left)

    if(node.visited is not True):
        printTree(node.right)

    print("Node=", node)
    node.visited = True


root = Node(3)
lnode = Node(2)
rnode = Node(4)
lchild = Node(1)
rchild = Node(5)
seven = Node(7)
rchild.left = seven
lnode.left = lchild
lnode.right = rchild
root.addleftChild(lnode)
root.addrightChild(rnode)
printTree(root)


def doit(curnode, lnum, rnum, lf, rf):
    if curnode is None:
        return None, 0

    if curnode.cargo == lnum or curnode.cargo == rnum:
        lf = 1
        print("matched at node {}".format(curnode.cargo))
        print("returning lf = {}".format(lf))
        return curnode, lf
    node, lf = doit(curnode.left, lnum, rnum, lf, rf)
    print("lf after calling left tree traversal with curnode = {} lf ={}".format(curnode.cargo,lf))
    rf = 0
    node, rf = doit(curnode.right, lnum, rnum, lf, rf)

    print("rf after calling left tree traversal with curnode = {} rf ={}".format(curnode.cargo,rf))
    if lf == 1 and rf == 1:
        print("Found the lowest parent {}".format(curnode.cargo))
        sys.exit(0)

    if lf == 1: 
        print("found only lf at node {}".format(curnode.cargo))
        return Node, lf
    if rf == 1: 
        print("found only rf at node {}".format(curnode.cargo))
        return Node, rf
    print("Nothing found returning at the bottom")
    return None, 0


def findcommonparent(root):
    leftfound = 0
    rightfound = 0
    print("doing it")
    doit(root, 1, 7, leftfound, rightfound)

findcommonparent(root)
