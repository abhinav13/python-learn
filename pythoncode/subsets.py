#! /usr/bin/python

try:
	a=[1,2,3,4]
	b=[5,6,7,8]
	c=[(x,y) for x in a for y in b]
	#print c
except ValueError:
	print "Value Error"


def insert_elements(dest, source):

    myset = set()
    for i in source:
        myset.add(i)
    dest.add(myset)
    return dest

l = [1,2,3,4]
j = []
k = []

for x in range(len(l)):
    j.append(x)

    for z in range(x+1,len(l)):
        for y in range(z+1,len(l)):

            k.append(l[z:y])
        k.append(l[x])
    j.append(k)
    k = []

print j
l=[1,2,3,4]
powerset = []
currentset = []


print l
def get_subset(j,k,l):
    """ This helper function returns a subset from the
        current list, if j and k are the same, then the element
        at that location is returned
    """
    ret_list = []
    if j == k:
        ret_list.append(l[j])
    else:
        for z in range(j,k+1):
            ret_list.append(l[z])
    return ret_list

for i, element in enumerate(l):
    currentset.append(element)
    powerset.append(currentset)
    for j in range(i+1, len(l)):
        for k in range(j,len(l)):
            temp = get_subset(j,k,l)
            temp.insert(0,element)
            powerset.append(temp)
    currentset = []
#Append the empty set
powerset.append([])
print powerset
