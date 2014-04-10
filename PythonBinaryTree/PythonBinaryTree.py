
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

    print node
    if(node.left != None):
        printTree(node.left)
   
    if(node.right != None):
        printTree(node.right)


headNode = Node("1")
leftChild = Node("2")
rightChild = Node("3")




current_sum=0;
#print lines
running_sum=0

def calculatesum(lines,running_sum):
    i=0;
    global current_sum
    if len(lines) != 0:

        for element in lines:
            print "current element",element  
            current_numbers = element.split()
            for n in current_numbers:
                print "current n", n
                running_sum = int(running_sum) + int(n)
                print "running_sum",running_sum
                #Recurse one level down
                newline = lines[i+1:]
                print newline
                print "Recursion begins"
                calculatesum(newline,running_sum)
                running_sum = running_sum - int(n) # reset our total 
            i=i+1        
    elif running_sum >= current_sum:
        print "lines were zero, running sum was greater than current_sum"
        current_sum = running_sum
    else:
        print "running_sum end of recursiong " , running_sum


lines = [line.strip() for line in open('sample.txt')]

calculatesum(lines,running_sum)
print "current_sum", current_sum


headNode.addleftChild(leftChild)
headNode.addRightChild(rightChild)

