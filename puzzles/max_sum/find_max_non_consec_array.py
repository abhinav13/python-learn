
import os

def max_non_consec(a,num):
	
	if(len(a) == 0):
		print "Empty a inserting num ", num
		a= []
		a.append(num)
	elif a[len(a)-1]-int(num) == -1 or a[len(a)-1]-int(num) == 1:
		print "Found consecutive numbers"
		if a[len(a)-1] < num:
			print "Replacing with highest of consec number " , num
			a[len(a)-1] = num
			print "After replacement " ,a
	else:
		a.append(num)
	return a

def max_list(prev_max, max_so_far):
	
	tot = 0
	
	for a in prev_max:
		tot = tot+int(a)
	prev_tot = 0
	for a in max_so_far:
		prev_tot = prev_tot + int(a)
	if(tot > prev_tot):
		return prev_max
	else:
		return max_so_far

def find_max_non_consec(a):
	max_so_far = prev_max = []
	
	for num in a:
		prev_max = max_non_consec(prev_max,num)
		print "prev max " , prev_max
		max_so_far = max_list(prev_max,max_so_far)
	return max_so_far

a = [2,3,4,7]

print find_max_non_consec(a)
			
