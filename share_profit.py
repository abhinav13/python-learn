#! /usr/bin/python

list = [7,6,5,5,4,1]
#list = [1,2,3,4,6,5]
maxprofit =list[0]-list[1]
cur_buyprice = list[0]
#sellprice= list[0]
#print maxprofit
for i in range(len(list))[1:]:
	print "i=",i
	if(cur_buyprice >= list[i] and i != len(list)-1):
		curprofit = list[i]-cur_buyprice
		if(curprofit > maxprofit):	
			cur_buyprice=list[i]
			print "Changed cur_buyprice = ",cur_buyprice

	if('maxprofit' not in locals()):
		maxprofit = curprofit
	elif (maxprofit <= curprofit ):
		sellprice = list[i]
		maxprofit = curprofit

	print "buyprice = ", cur_buyprice
	if('maxprofit' in locals() and 'sellprice' in locals()):
		print "sellprice = ",sellprice
		print "maxprofit = ",maxprofit
print "buyprice = " ,cur_buyprice
if('maxprofit' in locals() and 'sellprice' in locals()):
	print "sellprice = ",sellprice
	print "maxprofit = ",maxprofit
