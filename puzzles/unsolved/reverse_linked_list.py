class Node:

    def __init__(self):
        self.holder = 0
        self.next = None


myobj = Node()
myobj.holder = 1
myobj2 = Node()
myobj2.holder = 2
myobj.next = myobj2
tempobj = myobj

while tempobj != None:
    print(tempobj.holder)
    tempobj = tempobj.next
