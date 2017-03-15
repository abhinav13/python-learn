#! /usr/bin/python

try:
	a=[1,2,3,4]
	b=[5,6,7,8]
	c=[(x,y) for x in a for y in b]
	#print c
except ValueError:
	print( "Value Error")


def insert_elements(dest, source):

    myset = set()
    for i in source:
        myset.add(i)
    dest.add(myset)
    return dest


def swap(array, i, j):
    n = array
    n[i],n[j] = n[j],n[i]
    return n

def print_subset(array,start_index):

    """ This helper function returns a subset from the
        current list, if j and k are the same, then the element
        at that location is returned
    """

    if start_index == len(array):
        print("Returning as we reached the end ")
        return

    i = start_index
    j = i+1
    while i < len(array)-1:
        while j <=len(array)-1:
            print(array)
            array = swap(array, i, j)
            #print("after swapping callig subset",array)
            print_subset(array, start_index+1)
            array = swap(array, j, i)
            #print("swapping back",array)
            j=j+1
            #print("j=",j)
        i = i+1
        j = i+1
        #print("i=",i)
    return

l=[1,2,3]
print_subset(l,0)
