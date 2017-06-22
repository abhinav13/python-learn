import sys

def answer(s):
# your code here
    print s
    mydict =\
    {'a':'z',
    'b':'y',
    'c':'x',
    'd':'w',
    'e':'v',
    'f':'u',
    'g':'t',
    'h':'s',
    'i':'r',
    'j':'q',
    'k':'p',
    'l':'o',
    'm':'n',
    'n':'m',
    'o':'l',
    'p':'k',
    'q':'j',
    'r':'i',
    's':'h',
    't':'g',
    'u':'f',
    'v':'e',
    'w':'d',
    'x':'c',
    'y':'b',
    'z':'a'}
    outstring = ""
    for c in s:
        if c in mydict.keys():
            outstring = outstring + str(mydict[c])
        else:
            outstring = outstring + str(c)
    return outstring

print answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
print answer("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
