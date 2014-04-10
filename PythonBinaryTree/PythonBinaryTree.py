
class Node():
  
    def __init__(self, cargo=None,left=None, right=None):
        self.cargo = cargo
        self.left = left;
        self.right = right;
    
                   
    def __str__(self): 
        return str(self.cargo)            
                               
    def addleftChild(self, lchild):
        self.left = lchild

    def addRightChild(self, rchild):
        self.right = rchild



def printTree(node):

    if(node.left != None):
        printTree(node.left)
    print node
    if(node.right != None):
        printTree(node.right)


headNode = Node("1")
leftChild = Node("2")
rightChild = Node("3")

headNode.addleftChild(leftChild)
headNode.addRightChild(rightChild)

printTree(headNode)