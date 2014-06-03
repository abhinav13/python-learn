#! /usr/bin/python


phone_numbers = {
		 '1':None,
		 '2':"abc",
		 '3':"def",
		 '4':"ghi"
}
biglist=[]

for k in phone_numbers.keys():
	#Now create a list with values
	value = phone_numbers[k]
	if value != None:
		biglist.append([x for x in value])
ll=[(x,y,z) for x in biglist[0] for y in biglist[1] for z in biglist[2]]
print ll	
#print biglist
	
