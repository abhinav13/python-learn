import os
import sys


def calprod(numarray, start, end):
	total =1
	while(start <= end):
		total = total*int(numarray[start])
		start = start +1
	return total

def greaterthan(numarray,start,end, num):
	while(start <= end):
		if int(numarray[start]) < int(num):
			return True
		else:
			start = start+1
	return False

#This is inefficent as I am reading all the lines at once
#I can read this line by line and as I read the lines, I can
# add them to the list of the big number

with open("ProjEuler_Question8_input.txt",'r') as f:
	alllines = f.readlines()

numberlist = []

for line in alllines:
	line.rstrip()
	for digits in line:
		if digits.isdigit():
			numberlist.append(digits)
print "input array " , numberlist
start = 0
end =12
max_prod = calprod(numberlist, start,end)
frame_start = start+1
frame_end = end+1

while(frame_end < len(numberlist)):
	

	#now check if the new number that came in range is bigger than 
	#any number in the current frame of reference
 	if greaterthan(numberlist,start,end,numberlist[frame_end]):
		#we found a new max prod
		temp = calprod(numberlist,frame_start,frame_end)
		if(temp > max_prod):
			max_prod = temp
			start = frame_start
			print 'max frame_start', frame_start,'max frame end',frame_end
			print numberlist[frame_start:frame_end+1]
			print "max_prod",max_prod
			end = frame_end
	
	frame_end = frame_end +1
	frame_start = frame_start +1
	
print "max_prod of array ", max_prod	
