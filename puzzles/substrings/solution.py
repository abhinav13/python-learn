from functools import reduce

def get_largest_repeated_substring(input_str):
    d={}
    templist = [input_str[x:y] for x in range(len(input_str)+1) for y in range(len(input_str)+1) ]
    combolist = list(filter(None,templist)) #removes empty string
    #now make a dictionary out of these 
    for x in combolist:
        if(x not in d.keys()):
            d[x] =1
        else:
            d[x] = int(d[x])+1
    #now look at keys and their value and find the key with the highest value and key length
    longest_key = list(d.keys())[0]
    highest_value = d[longest_key]

    for k,v in d.items():
        if len(k) > len(longest_key) and int(v) > int(highest_value):
            highest_value = v
            longest_key = k

    return longest_key,highest_value

string = "ABCDEABCD"

key,value = get_largest_repeated_substring(string)
print(key,value)

