import sys,re
import getopt
import os


def count_unique_alphabets_in_each_word(word):
    output_word=''
    if(len(word) == 1):
        return word
    #if we have two characters, we know it is going to be A0B for e.g. AB will always give A0B
    if(len(word) == 2):
        output_word = ''.join([word[0],'0',word[1]])
        return output_word
        
    d={}
    output_word = word[0]
    for i,c in enumerate(word[1:len(word)-1]): #traverse all the way upto 2nd last character
        d[c.upper()]=1 
    #now join the lenght of the dictionary along with the last character in the word to output
    output_word = ''.join([output_word,str(len(d)),word[len(word)-1]])
    return output_word
    
def process_words(word):
    """ This functions sperates each word in to a list of consecutive alphabets and non alphabets """
    if(word is None or len(word) == 0 or len(word)==1 ):
        return word
    array= list(filter(None,re.split(r'([A-Za-z]+)',word))) #Create a list of alphabets and non alphabet characters
    for i,word in enumerate(array):
        if(word.isalpha()): #word contains only alphabets
            array[i] = count_unique_alphabets_in_each_word(word)
    return (''.join(array))

    
def solve(input_file,output_file):
   
   #Check if input file exists, if not thrwo and exception and get out

    if( not os.path.isfile(input_file)):
        print("Input file does not exist in the current directory")
        exit(-1)
    with open(output_file, 'w'): pass   ##Clear out previous content of output file

    with open(input_file, 'r') as f:
        with open(output_file,'a') as out_fp:
            for line in f:
                output_string=""
                array= re.split(r'(\s+)',line.strip())
                array = list(filter(None,array)) #Remove Empty elements from the array
                for i,word in enumerate(array):
                    str_word = str(word)
                    #Call Create String only if this word is not a white space
                    if(len(str_word) != 0 and not str_word.isspace()):
                        output_string = process_words(str_word)
                        array[i]=output_string
                #now write this into output file
                out_fp.write(''.join(array))
                out_fp.write('\n')


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
