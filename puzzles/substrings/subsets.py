#! /usr/bin/python
#Easy Given a list of two integers or set of two integers, print all two number subsets from this list of integers
#Hard- Print all subsets from a given set of two integers.

try:
	a=[1,2,3,4]
	b=[5,6,7,8]
	c=[(x,y) for x in a for y in b]
	print( c)
except ValueError:
	print( "Value Error")


def print_subsets_of_array(array):

    for i, el in enumerate(array):

