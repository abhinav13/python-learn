#This program recursively Calculates from a series of numbers in a file which are read into lists of lists

largest_sum=0;
#print lines
running_sum=0


def calculatesum(lines,running_sum):
    i=0;
    global largest_sum
    if len(lines) != 0:

        for element in lines:
            print "current element",element  
            current_numbers = element.split()
            for n in current_numbers:
                print "current n", n
                running_sum = int(running_sum) + int(n)
                print "running_sum",running_sum
                #Recurse one level down
                newline = lines[i+1:]
                print newline
                print "Recursion begins"
                calculatesum(newline,running_sum)
                running_sum = running_sum - int(n) # reset our total 
            i=i+1        
    elif running_sum >= largest_sum:
        print "lines were zero, running sum was greater than largest_sum"
        largest_sum = running_sum
    else:
        print "running_sum end of recursiong " , running_sum

#Read the lines into a list

lines = [line.strip() for line in open('sample.txt')]


calculatesum(lines,running_sum)
#debug print
#print lines
