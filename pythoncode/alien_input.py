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
    parser = argparse.ArgumentParser(description='Read the questions for more info')
    parser.add_argument('-f', metavar='ARG1', type=str, nargs='*',help='input file containing translation key and alien input')
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
    return

def create_translation_dict(line):
    temp = line.split()
    translation_dict = {}
    for k in range(0,len(temp),2):
        translation_dict[temp[k+1]] = temp[k]
    return translation_dict

def main():

    #Read the input file
    rest_of_the_input=""
    with open(get_sourcefilename() + ".txt", 'r') as f:
        rest_of_the_input = f.read().rstrip()
        print(rest_of_the_input)

    with open(get_sourcefilename()+"_keys.txt", 'r') as f:
        first_line = f.read().rstrip()
        translation_dict = create_translation_dict(first_line) 
        print(translation_dict)
        word = ""
        for i,item in enumerate(rest_of_the_input):
            if(item.isalnum()):
                word = "".join((word,item))
                #now check it in our look up dictionary if a transaltion exists
                if(word in translation_dict):
                    print(translation_dict[word],end='')
                    word = ''
            else:
                print(item,end='')
    print()
if __name__ =="__main__":
    main()
	

