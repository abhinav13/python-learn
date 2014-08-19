import os
import inspect
import logging
import argparse
from enum import Enum


functionlookup = {'DEBUG': lambda x: logging.debug(x), 'WARN': lambda x : logging.warn(x), 'INFO': lambda x : logging.warn(x) }


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
	""" Class Init """
	def __init__(self,filename=None, loglevel=None):
		if filename == None:
			filename = get_logfileName()
		if loglevel == None:
			loglevel = 'DEBUG' 
		elif not isinstance(getattr(logging,loglevel.upper(),None), int):
			raise ValueError('Invalid Log Level specified :%s' %loglevel)

		self["filename"] = filename
		self["loglevel"] = loglevel
		logging.basicConfig(filename = self.filename, filemode='w', format='%(asctime)s %(message)s', 
				    datefmt='%m/%d/%Y %I:%M:%S %p', level=loglevel.upper())

	"""This function writes to a log file """
	def write(loglevel,message):
		if self["loglevel"] == loglevel:

		



def Mylog(input, loglevel):



def main():
	inputfile = Create_InputFileName()




if __name__ =="__main__":
	main()
	

