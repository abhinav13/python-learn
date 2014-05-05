import sys

class Node():
  
    def __init__(self, cargo=None,left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        self.visited = None
	self.sumbelow = 0
                   
    def __str__(self): 
        return str(self.cargo)            
                              
    def addleftChild(self, lchild):
        self.left = lchild

    def addrightChild(self, rchild):
        self.right = rchild

    def __getitem__(self,item):
        return self


def printTree(node):

    if(node == None):
        return
    if(node.visited != True):
        printTree(node.left)
   
    if(node.visited != True):
        printTree(node.right)

    print "Node=", node,
    node.visited = True; 


#Read the lines into a list

lines = [line.strip() for line in open(sys.argv[1])]
print lines
#Init head of tree = None
head=None

total=0
prev_total =0
#Calculate largest sum seen so far
def calsum(node):
	#recurse through the tree
	global total
	#current_num = node.cargo
	global prev_total
	if(node == None):
		#we have reached the end. So now calculate the sum and store it in a list
		if prev_total == 0:
			prev_total = total
		elif prev_total < total:
			prev_total = total
		return
	#Add the node's value to total and recurse left side
	#now only visit the left tree if we have not calculated the sum below this node
	if node.sumbelow != 0:
		#we dont need to traverse down the tree
		total = total+node.sumbelow 
	else:
		calsum(node.left)
		total = total+int(node.cargo)
	#subtract the left child's value from the total and call right child
	if(node.left != None):
		total = total - int(node.left.cargo)
		print "Subtracting left child", node.left.cargo
		#now calculate the sum of nodes below this node.
		if int(node.cargo) + int(node.left.cargo) > int(node.sumbelow):
			node.sumbelow = int(node.cargo) + int(node.left.cargo)
	calsum(node.right)
	
	if(node.right != None):
		total = total - int(node.right.cargo)
		print "Subtracting right child",node.right.cargo
		if int(node.cargo) + int(node.right.cargo) > int(node.sumbelow):
			node.sumbelow = int(node.cargo) + int(node.right.cargo)
	#now mark the node as visited
	return	
		
def createTree(lines):
        global head
        line_number=0
        element_number=0
        nodeList=[] #This contains parent nodes
        i=0 #This keeps track of which parent Row are on
        for line in lines:
               #see if this is the first line by looking at the length of the line
               current_numbers = line.split()
               print "current_numbers", current_numbers
               if len(current_numbers) == 1:
                   head = Node(current_numbers[0])
                   nodeList.insert(line_number,head)
               else:
                   #This is the second line, this means we need to go create nodes one by oneand attach them to their parents
                   j=0  # This keeps track of the numbers that we are currently processing
                   second_row=[]
                   for number in current_numbers:
                       print "j= ",j, "current number = " , number
                       parentRow = nodeList[i-1] #This is the row of nodes that are the parents
                       
                       newNode = Node(number)
                       if j==0:
                           #left most child
                                                                      
                           print "Inserting Left Most Child which is number ", number, "Into parent Node " , parentRow[j]
                           parentRow[j].addleftChild(newNode) #Attach as the left child of the first Node parent row
                       elif j == len(current_numbers)-1: #This is the last node in the current children, so this can only be attached as the right child of the parent node
                
                           print "Inserting Right Most Child which is number ", number, "Into parent Node " , parentRow[j-1]
                           parentRow[j-1].addrightChild(newNode)
                       else:
                           
                           #Attach it as the left child of the Node in the parent list which is one less than the Child's current index
                         
                           print "Inserting Right  Child which is number ", number, "Into parent Node " , parentRow[j-1], "And Left Child into Parent ", parentRow[j]
                           parentRow[j-1].addrightChild(newNode)
                           #This node the left child of the parent node which has the same index as its own
                           parentRow[j].addleftChild(newNode)

                       second_row.insert(j,newNode) 
                       j = j +1
                   #Now insert these parents in the NodeList
                   nodeList.insert(i,second_row)     
               i = i +1

#Create the Binary Tree from the File
createTree(lines)
printTree(head)
calsum(head)
print "total", total
print "prev_total", prev_total
