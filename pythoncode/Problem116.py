

def  createArray(size):
	
	a = []
	for x in range(0,int(size)):
		a.append('O')
	return a


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
	

print createArray(5)
b = ['R','R']

fillArray(createArray(5),b)
