#!/usr/bin/python
import random

d={}

UpperLimit = 100
LowerLimit = 0

def generateNum(UpperLimit, LowerLimit):
	global d	
	
	for i in range(0,50):
		num = random.randrange(LowerLimit,UpperLimit)
		d[str(num)] = num

	print d


def findinlist(num):
	global UpperLimit
	global LowerLimit
	print "Finding closest match for ", num
	if str(num) in d.keys():
		print "found exact match ", num
		return num
	uppernum=num
	lowernum=num
	found = False
	u_ret_val = UpperLimit+1
	l_ret_val = LowerLimit-1
	#now start walking up the list and down the list to find the next closest match
	while uppernum <= UpperLimit or lowernum >= LowerLimit:
		print "uppernum", uppernum, "lowernum", lowernum
		if str(uppernum) in d.keys():
			u_ret_val = uppernum	
			found = True 
		if str(lowernum) in d.keys():
			l_ret_val = lowernum
			found = True 
					
		if found == True:
			break
		uppernum = uppernum +1
		lowernum = lowernum -1	
	# now see what did we actually find, lower number or higher number 
	if l_ret_val == LowerLimit-1:
		print "Found a Upper number", u_ret_val
		return u_ret_val
	#We always return the lower number
	else:
		print "Found a lower number", l_ret_val
		return l_ret_val


d={'0':0,'100':100}
print d
print findinlist(90)

d= {'0':0,'100':100}
print d
print findinlist(0)


d= {'0':0,'100':100}
print d
print findinlist(10)

d= {'0':0,'100':100}
print d
print findinlist(100)
d={'89':89,'91':91}
print d
print findinlist(90)

d={'10':10,'91':91}
print d
print findinlist(0)

generateNum(UpperLimit,LowerLimit)

for i in xrange(0,50):
	num = random.randrange(LowerLimit,UpperLimit)
	print findinlist(num)
