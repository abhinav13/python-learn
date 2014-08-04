import os
import sys


def calprod(l, start, end):
	total =1
	while(start != end):
		total = total*int(l[start])
		start = start +1
	return total

def greaterthan(l,start,end, num):
	print "now scanning",start,"to end", end, "for number", num	
	while(start <= end):
		if int(l[start]) < int(num):
			return True
		else:
			start = int(start)+1
	print "exit"
	return False

#This is inefficent as I am reading all the lines at once
#I can read this line by line and as I read the lines, I can
# add them to the list of the big number

with open("question8.txt",'r') as f:
	d = f.readlines()
	#print d
	#print type(d)

numberlist = []

for line in d:
	line.rstrip()
	for digits in line:
		if digits.isdigit():
			numberlist.append(digits)
print numberlist
start = 0
end = 12
max_prod = calprod(numberlist, start,end)
print "max_prod",max_prod
frame_start = start
frame_end = start
print len(numberlist)
while(frame_end < len(numberlist)):
	

	#now check if the new number that came in range is bigger than 
	#any number in the current frame of reference
 	if greaterthan(numberlist,start,end,numberlist[frame_end]):
		#we found a new max prod
		max_prod = calprod(numberlist,frame_start,frame_end)
		start = frame_start
		print "max_prod",max_prod
		end = frame_end
	else:
		print "no go"
	print 'current frame end',frame_end
	frame_end = frame_end +1
	frame_start = frame_start +1
	
print max_prod	
