import sys

# This program divides a number by the divisor without using the divison operator and returns the mantissa and 
# not the remainder
#Arg 1 is the number to divide
# Arg2 is the divisor 

def divby7(number,divisor):
	i=1
	divisor=7	
	count = divisor
	if  divisor > number:
		return 0 
	while count < number:
		count = count << 1 
		i = i << 1
	if count == number:
		return i
    	elif count > number:
        #while count > number subtracting count and keep track
        	while count > number :
            		count = count -divisor
            		i = i-1
    	return i   

print divby7(int(sys.argv[1]),int(sys.argv[2]))
