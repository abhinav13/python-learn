#! /usr/bin/python

try:
	a=[1,2,3,4]
	b=[5,6,7,8]
	c=[(x,y) for x in a for y in b]
	print c
except ValueError:
	print "Value Error"
