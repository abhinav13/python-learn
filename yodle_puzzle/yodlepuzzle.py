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
		self.Value = int(self.HValue) + int(self.PValue) + int(self.EValue) + int(self.HValue)	


	def __str__(self):
		return "Name %s, HValue %s, EValue %s, PValue %s Value %s" % \
			(self.Name,self.HValue,self.EValue,self.PValue,self.Value) 
class Juggler:
	
	def __init__(self,line):
		if(len(line) == 0 or str(line[0]).upper() != 'J'):
			print "Incorrect input to Juggler class"
			exit()

		newline = line[1:].lstrip()
		(CName,H,E,P,Pref) = newline.split()
		self.Name = CName
		self.HValue = H.split(':')[1]
		self.EValue = E.split(':')[1]
		self.PValue = P.split(':')[1]
		self.PrefList = []
		self.PrefList = Pref.split(',') 
		self.Value = int(self.HValue) + int(self.PValue) + int(self.EValue) + int(self.HValue)	


	def __str__(self):
		return "Name %s, HValue %s, EValue %s, PValue %s Value %s PrefList %s" % \
			(self.Name,self.HValue,self.EValue,self.PValue,self.Value, self.PrefList) 


if (len(argv) != 2) :
	print "Usage: yoddle_puzzle.py <inputfile.txt>"
	exit()

with open(argv[1], 'r') as f:
	for line in f:
		if(len(line.strip()) != 0 and str(line[0]).upper() == 'C'):
			print Circuit(line)
		elif (len(line.strip()) != 0 and str(line[0]).upper() == 'J'):
			print Juggler(line)
		else:
			print "Found Empty Line"
