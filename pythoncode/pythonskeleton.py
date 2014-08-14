import os
import inspect
import logging
import argparse
from enum import Enum

class LogLevel(Enum):
	debug =1
	error=2
	info = 3
	critical = 4


"""Return the Input File for this file """
def get_sourcefilename():
	filename,extension = (inspect.getfile(inspect.currentframe())).split('.')
	return filename 

def get_logfilename():
	return get_sourcefilename + ".log"



class MyLog:
	"""This prints to a log file """
	def __init__(self,filename=None, loglevel=None):
		if filename == None:
			filename = get_logfileName()
		if loglevel == None:
			loglevel = 'DEBUG' 

		self["filename"] = filename
		self["loglevel"] = loglevel

	def write(loglevel,message):
		if self["loglevel"] == loglevel:

		



def Mylog(input, loglevel):



def main():
	inputfile = Create_InputFileName()




if __name__ =="__main__":
	main()
	

