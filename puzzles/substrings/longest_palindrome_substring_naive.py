# Problem2: Find the longest palindromic substring in a string of characters
from collections import defaultdict

def ifpalindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True




def checkpalindromes(l):
    d = defaultdict(list)
    for s in l:
        if ifpalindrome(s):
            d[len(s)].append(s)
    return d

l="ABCDEEEEFGHIJKLLLLLLMKO"
biglist = [ x+"".join(l[i+1:y]) for i, x in enumerate(l) for y in range(i+1,len(l)+1) if len(l[i+1:y]) > 0 ]

output_dict = checkpalindromes(biglist)
#max_len = max(k,v for k,v in output_dict.items())
max_len = max(output_dict.iterkeys())
print(max_len, output_dict[max_len])
