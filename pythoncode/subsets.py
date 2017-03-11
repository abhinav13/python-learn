#! /usr/bin/python

try:
	a=[1,2,3,4]
	b=[5,6,7,8]
	c=[(x,y) for x in a for y in b]
	print c
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
