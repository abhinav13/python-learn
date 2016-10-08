import sys,re
import getopt
import os

def count_letters(word):

    if(len(word) == 1 or word is None or len(word) == 0):
        return word
    output_string=''
    anchor_pos = 0
    anchor_set = False 
    d ={} 
    for i,c in enumerate(word):
    #now walk the string
        if(not c.isalpha()):
            #Check if we were in the middle of counting character by checking on our anchor
            if(not anchor_set):  #we are not in the middle of counting alphabets
                output_string = ''.join([output_string,str(c)])
            else:
                #we were in the middle of counting characters and found a non alpha character
                #did we only see two alphabets before this non alphabet character ? for e.g. 11AB7
                #This should print only 11A0B7. Check the length of the dict
                if( len(d) == 0):
                    output_string = ''.join([output_string,str(word[anchor_pos]),str(len(d))])
                else:
                    output_string = ''.join([output_string,str(word[anchor_pos]),str(len(d)-1),str(word[i-1])])
                output_string = ''.join([output_string,c])
                #reset anchor and empty dictionary
                anchor_set=False
                d={}
        elif(i+1 == len(word)):    #did we reach the end of the string
            output_string = ''.join([output_string,word[anchor_pos],str(len(d)),c])
        elif(not anchor_set):  #we are starting out for the first time
            anchor_pos=i
            anchor_set = True
            d={}
        else:
            d[c]=1

    return output_string



def solve(input_file,output_file):
   
   #Check if input file exists, if not thrwo and exception and get out

    if( not os.path.isfile(input_file)):
        print("Input file does not exist in the current directory")
        exit(-1)
    with open(output_file, 'w'): pass   ##Clear out previous contenet of output file
    with open(input_file, 'r') as f:
        with open(output_file,'a') as f2:
            for line in f:
                output_string=""
                array= re.split(r'(\s+)',line.strip())
                array = list(filter(None,array)) #Remove Empty elements from the array
                print("input array", array)
                for i,word in enumerate(array):
                    str_word = str(word)
                    #Call Create String only if this word is not a white space
                    if(len(str_word) != 0 and not str_word.isspace()):
                        output_string = count_letters(str_word)
                        print("output ",output_string)       
                        array[i]=output_string
                print("output array", array)
                #now write this into output file
                f2.write(''.join(array))
                f2.write('\n')


def print_usage():
    print("solution.py -i <inputfile> -o <outputfile>")


def main():

    inputfile=""
    outputfile=""
    try:
        opts,remaining_args = getopt.getopt(sys.argv[1:],"hi:o:")
    except getopt.GetoptError:
        print_usage()
        exit(1)
    if(len(opts) == 0 ):
        print_usage()
        exit(1)
    for option, argvalue in opts:
        if option == '-h':
            print_usage() 
            exit(1)
        elif option == '-i':
            inputfile = argvalue
        elif option == '-o':
            outputfile = argvalue
    
    if(len(inputfile) == 0 or (len(outputfile)==0)):
        print_usage()
        exit(1)
    solve(inputfile,outputfile)

if __name__ == "__main__":
    main()
