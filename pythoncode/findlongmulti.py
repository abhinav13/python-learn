import os
import inspect
import re


def Cal_Product(numbers):
	ret_val = 1
	for digit in numbers:
		ret_val = ret_val*int(digit)
	return ret_val

#Read the number in a list
filename,extension = (inspect.getfile(inspect.currentframe())).split('.')
filename = filename+"_input.txt" 
print filename 
fo = open(filename)
bignum=[]
bignum = fo.readlines()
allnum=[]

for digits in bignum:
	for number in digits:
		allnum.append(number)
print allnum

digits = allnum[:13]
cur_max = Cal_Product(digits)

remaining_array = allnum[14:]
window_begining = 1
window_end = window_begining + 13


	
