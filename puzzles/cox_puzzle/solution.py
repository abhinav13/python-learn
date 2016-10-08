import sys,re
import getopt



def count_letters(word):

    if(len(word) == 1 or word is None or len(word) == 0):
        return word
    print("input ", word)
    output_string=''
    anchor_pos = 0
    anchor_set = False 
    d ={} 
    for i,c in enumerate(word):
    #now walk the string
        print("c= ",c)
        if(not c.isalpha()):
            #Check if we were in the middle of counting character by checking on our anchor
            if(not anchor_set):  #we are not in the middle of counting alphabets
                print("Anchor noet set")
                output_string = ''.join([output_string,str(c)])
                print(output_string)
            else:
                #we were in the middle of counting characters and found a non alpha character
                print("Anchor was set")
                #did we only see two alphabets before this non alphabet character ? for e.g. 11AB7
                #This should print only 11A0B7. Check the length of the dict
                if( len(d) == 1):
                    output_string = ''.join([output_string,str(word[anchor_pos]),str(len(d)-1),str(word[i-1])])
                elif(len(d) == 0 ): ##This is the case for 11A7
                    output_string = ''.join([output_string,str(word[anchor_pos]),str(len(d))])
                output_string = ''.join([output_string,c])
                #reset anchor and empty dictionary
                anchor_set=False
                d={}
        elif(i+1 == len(word)):    #did we reach the end of the string
            print("Reached End of string")
            output_string = ''.join([output_string,word[anchor_pos],str(len(d)),c])
            print(output_string)
        elif(not anchor_set):  #we are starting out for the first time
            anchor_pos=i
            anchor_set = True
            print("Setting anchor first time")
            d={}
        else:
            d[c]=1
        print("Current output ", output_string)
        print("Current dic", d)
    return output_string



def solve(input_file,output_file):
    
    with open(input_file, 'r') as f:
        for line in f:
            output_string=""
            array= re.split(r'(\s+)',line.strip())
            print("array = ", array)
            for word in array:
                str_word = str(word)
                #Call Create String only if this word is not a white space
                if(len(str_word) != 0 and not str_word.isspace()):
                    output_string = count_letters(str_word)
                    print("output ",output_string)       

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
