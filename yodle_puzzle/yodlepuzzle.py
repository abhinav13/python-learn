#C C0 H:7 E:7 P:10
#C C1 H:2 E:1 P:1
#C C2 H:7 E:6 P:4

#J J0 H:3 E:9 P:2 C2,C0,C1
#J J1 H:4 E:3 P:7 C0,C2,C1
#J J2 H:4 E:0 P:10 C0,C2,C1
#J J3 H:10 E:3 P:8 C2,C0,C1
#J J4 H:6 E:10 P:1 C0,C2,C1
#J J5 H:6 E:7 P:7 C0,C2,C1
#J J6 H:8 E:6 P:9 C2,C1,C0
#J J7 H:7 E:1 P:5 C2,C1,C0
#J J8 H:8 E:2 P:3 C1,C0,C2
#J J9 H:10 E:2 P:1 C1,C2,C0
#J J10 H:6 E:4 P:5 C0,C2,C1
#J J11 H:8 E:4 P:7 C0,C1,C2

import os
from sys import argv	

class Circuit:
	
	def __init__(self,line):
		if(len(line) == 0 or str(line[0]).upper() != 'C'):
			print "Incorrect input to Circuit class"
			exit()

		newline = line[1:].lstrip()
		(CName,H,E,P) = newline.split()
		self.Name = CName
		self.HValue = H.split(':')[1]
		self.EValue = E.split(':')[1]
		self.PValue = P.split(':')[1]
		self.AssignedJugglers = []

	def __str__(self):
		return " %s" % \
			(self.Name) 
	
	def __repr__(self):
		return str(self) 
	
	def dotProduct(self,Juggler):
		return 	(int(self.HValue) * int(Juggler.HValue))+\
			(int(self.EValue) * int(Juggler.EValue))+\
			(int(self.PValue) * int(Juggler.PValue))

	def debugPrint(self):
		print 'HValue:r',self.HValue,'EValue:',self.EValue,'PValue:',self.PValue\
			,'JugglerList:',self.AssignedJugglers

class Juggler:
	
	def __init__(self,line,AllCircuits):
		if(len(line) == 0 or str(line[0]).upper() != 'J'):
			print "Incorrect input to Juggler class"
			exit()

		newline = line[1:].lstrip()
		(CName,H,E,P,Pref) = newline.split()
		self.Name = CName
		self.HValue = H.split(':')[1]
		self.EValue = E.split(':')[1]
		self.PValue = P.split(':')[1]
		self.PreferedCircuits = []
		self.PreferedCircuits = [ AllCircuits[x] for x in Pref.split(',') ] 


	def __str__(self):
		return "JName %s, %s" % \
			(self.Name, [ (x.Name,':',x.dotProduct(self)) for x in self.PreferedCircuits])

	def __repr__(self):
		return str(self)


def findJugglertoReplace(Circuit, thisJuggler,JugglerList):

	b = [ (x, (Circuit.dotProduct(thisJuggler) - Circuit.dotProduct(x)))\
		 for x in JugglerList if (Circuit.dotProduct(thisJuggler) - Circuit.dotProduct(x)) >0 ]
	sorted_by_second = sorted(b, key=lambda tup: tup[1],reverse=True)
	print "sorted_by_second", sorted_by_second
	if(len(sorted_by_second) > 0 ):
		(juggler_to_return,score) = sorted_by_second[0]
	else:
		juggler_to_return = None
	return juggler_to_return	
		
	
def assignJuggler(AllCircuits,thisJuggler,limit):
#	if(len(self.AssignedJugglers) < limit):
# if the juggler's prefered circuit has less than limit jugglers assigned, then insert the juggler to this circuit
# if the juggler's prefered circuit has no space ,then see if the dot product of the juggler with this circuit 			
# is greater than any juggler in this circuit, the juggler with the score lower than current juggler is removed
# Now the circuit needs to be rebalanced. You take the removed juggler and look at its next preferred circuit
# if the next preferred circuit is full, you do the same trick of removal/addition. The juggler with the lowest score
# looses. And then he is assigned to it




	inserted=False
	#Check to see what the jugglers preference are
	for preferedcircuit in thisJuggler.PreferedCircuits:
		if(len(preferedcircuit.AssignedJugglers) < limit):
			print "Adding Juggler",thisJuggler.Name," to free circuit",preferedcircuit.Name,preferedcircuit.AssignedJugglers	
			preferedcircuit.AssignedJugglers.append(thisJuggler)
			inserted = True
			return None
		else: #
			#compare this jugglers match rating with all the ones in the preferred circuit
			removethisjuggler = findJugglertoReplace(preferedcircuit,thisJuggler,preferedcircuit.AssignedJugglers)
			if(removethisjuggler != None):
				print "Removing Juggler", removethisjuggler.Name,"from circuit",preferedcircuit.Name	
				preferedcircuit.AssignedJugglers.remove(removethisjuggler)
				print "Adding Juggler ", thisJuggler, "to circuit",\
				preferedcircuit.Name ,preferedcircuit.AssignedJugglers
				preferedcircuit.AssignedJugglers.append(thisJuggler)
				inserted = True	
				#Now Recursively call 
				#to Add the removed Juggler back into the circuits
				assignJuggler(AllCircuits,removethisjuggler,limit)
		if inserted == True:
			break
		return None



AllJugglers = {}
AllCircuits = {}

#Debug Prints

def PrintCircuits():
	for k in AllCircuits.keys():
		k.debugPrint()

def PrintJugglers():
	for k in AllJugglers.keys():
		print AllJugglers[k]


#Usage
if (len(argv) != 2) :
	print "Usage: yoddle_puzzle.py <inputfile.txt>"
	exit()

with open(argv[1], 'r') as f:
	for line in f:
		if(len(line.strip()) != 0 and str(line[0]).upper() == 'C'):
			c = Circuit(line)
			#Now add this to the dictionary
			AllCircuits[str(c.Name)] = c
		elif (len(line.strip()) != 0 and str(line[0]).upper() == 'J'):
			c = Juggler(line,AllCircuits)
			AllJugglers[str(c.Name)] = c
			

JugglersPerCircuit = len(AllJugglers.keys())/len(AllCircuits.keys())
print "Juggler per circuit", JugglersPerCircuit

for k in AllJugglers.keys():
	assignJuggler(AllCircuits,AllJugglers[k],JugglersPerCircuit)

for k in AllJugglers.keys():
	j = AllJugglers[k]
	print j.Name,
	for pref_circuit in j.PreferedCircuits:
		print pref_circuit,':',pref_circuit.dotProduct(j),	
	print


#PrintCircuits()
#PrintJugglers()
