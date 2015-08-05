import os
import inspect
import logging
from enum import Enum
import argparse


functionlookup = {'DEBUG': lambda x: logging.debug(x), 'WARN': lambda x : logging.warn(x), 'INFO':lambda x : logging.info(x)}

class LogLevel(Enum):
    debug =1
    error=2
    info = 3
    critical = 4

""" Return the Input File for this file """
def get_sourcefilename():
    filename,extension = (inspect.getfile(inspect.currentframe())).split('.')
    return filename 

def get_logfilename():
    return str(get_sourcefilename()) + str(".log")


class MyLog:
    """ Class Init """
    def __init__(self,filename=None, loglevel='DEBUG'):
        if filename == None:
            filename = get_logfilename()
        if not isinstance(getattr(logging,loglevel.upper(),None), int):
            raise ValueError('Invalid Log Level specified :%s' %loglevel)
        self.filename = filename
        self.loglevel = loglevel
        logging.basicConfig(filename = self.filename, filemode='w', format='%(asctime)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p', level=self.loglevel.upper())

    """This function writes to a log file """
    def write(self,loglevel,message):
        if loglevel.upper() not in functionlookup.keys():
            raise ValueError('Invalid Log Level specified :%s' %loglevel)
        else:
            functionlookup[loglevel.upper()](message)

        
def get_parser():
    parser = argparse.ArgumentParser(description='Put your description here')
    parser.add_argument('arg1', metavar='ARG1', type=str, nargs='*',help='Arg1 help text')
    parser.add_argument('-p', '--pos', help='Detail about first argument (default: 1)', default=1, type=int)
    parser.add_argument('-v', '--version', help='displays the current version of program',
                                    action='store_true')
    return parser

def  command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print("No Version Defined")
        return
    if args['arg1']:
        print("Arg1 Detected")
    return


def calculate_area(matrix):
    pass

def create_matrix(row, col):
    return [[0 for x in range(col)] for x in range(row)]


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element," ", end="")
        print(" ")

def insert_stickies(matrix, start_row, start_column, color, area):
    pass

def main():
    x = MyLog(loglevel="Debug")
    #command_line_runner()
    matrix = create_matrix(5,5)
    print_matrix(matrix)

if __name__ == "__main__":
    main()
	
	


	
	
	



