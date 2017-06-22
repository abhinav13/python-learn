

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
lnode.left = lchild
root.addleftChild(lnode)
root.addrightChild(rnode)
printTree(root)


def doit(curnode, lnum, rnum, lf, rf):
    if root is None:
        return

    if curnode.cargo == lnum:
        lf = 1
        print("lf is 1 now at node {}".format(curnode.cargo))
        return
    if curnode.cargo == rnum:
        print("rf is 1 now at node {}".format(curnode.cargo))
        rf = 1
        return
    doit(curnode.left, lnum, rnum, lf, rf)

    if lf == 1:
        print("found lf so passing 0")
        doit(curnode.right, lnum, rnum, 0, rf)
    else:
        doit(curnode.right, lnum, rnum, lf, rf)
    if lf == 1 and rf == 1:
        print("Found node {}".format(curnode.cargo))
    return


def findcommonparent(root):
    leftfound = 0
    rightfound = 0
    print("doing it")
    doit(root, 2, 4, leftfound, rightfound)

findcommonparent(root)
