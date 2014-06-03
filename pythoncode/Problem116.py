



def fillArray(array, fillwiththis):

	size = len(fillwiththis)
	start = 0
		
	while(start != len(array)):
		if(start + len(fillwiththis) > len(array)):
			break
		else:
			cursor = start
			for i in range(0,len(fillwiththis)):
				array[start] = fillwiththis[i]
			print array
			array = createArray(len(array))
			start = start+1			
	


import sys
def CreateArray(a,size,character='O'):
	a = [ character for x in range(0,int(size))]
	return a

def CalNumMethods(a,insertarray):

	start = 0
	#cursor = start
	while start != len(a):
		if (start + len(insertarray) > len(a)):
			break
		for i in range(0,len(insertarray)):
			a[start +i] = insertarray[i]
		start = start+1		

		print a
		a = CreateArray(a,len(a),'O')


size = sys.argv[1]
inputsize = sys.argv[2]
print size
a=[]
b=[]


a = CreateArray(a,size)
b = CreateArray(b,inputsize,'X')
print b
CalNumMethods(a,b)
