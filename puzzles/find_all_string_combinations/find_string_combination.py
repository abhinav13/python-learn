
def swap(a, i ,j):
	
	temp = a[int(i)]
	a[int(i)] = a[int(j)]
	a[int(j)] = temp



def findAll(a,start):
	
	#print "start at the begining ", start
	if(start > len(a)-1):
		return
	else:
		print a

	while(start < len(a)-1):
		j = start+1
		while j <= len(a)-1:
			print "Before swap a = " , a,
			print "j = ",j,"start = ",start
			swap(a,start,j)
			findAll(a,j)
			print "After recursive call a= ", a
			swap(a,j,start)
			print "After reverse swap a= ", a
			j = j+1
		start = start+1

a = ['A','B','C']

findAll(a,0)
