#Given a string, find all posssible combinations of the string.
#for e.g
#give ABC
#the output of the program should be
#ABC
#BAC
#BCA
#ACB
#CAB
#CBA

def swap(a, i ,j):

	temp = a[int(i)]
	a[int(i)] = a[int(j)]
	a[int(j)] = temp



def findAll(a,start):

	#print "start at the begining ", start
	if(start == len(a)-1):
		print "Returning aftger printing " ,a
		return

	j =start
	while j <= len(a)-1:
		#print "Before swap a = " , a,
		#print "j = ",j,"start = ",start
		swap(a,start,j)
		#print "Calling FinDAll "
		findAll(a,start+1)
		#print "After recursive call a= ", a
		swap(a,j,start)
		#print "After reverse swap a= ", a
		j = j+1


a = ['A','B','C']

findAll(a,0)
