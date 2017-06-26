
def stingy(number):
    num_persons = 2 
    a = 1
    b = 1
    c = 0
    temp = []
    temp.append(a)
    temp.append(b)
    lamb_remaining = number - (a+b)
    while c <= lamb_remaining:
        print "Before addding c={}".format(c)
        c = a + b
        print "After addding c={}".format(c)  
        if lamb_remaining >= c:
            temp.append(c)
            lamb_remaining = lamb_remaining - c 
            print "lamb_remaining = {}".format(lamb_remaining)
            num_persons = num_persons + 1
        a = b
        b = c
    return num_persons, temp


def generous(number):
    num_persons = 2
    a = 1
    b = a * 2
    temp = []
    temp.append(a)
    temp.append(b)
    lamb_remaining = number - (a + b)
    print "lamb_remaining before starting loop = {}".format(lamb_remaining)
    while b <= lamb_remaining:
        a = b
        b = a * 2
        print "after incrementing b = {}".format(b)
        print "lamb_remaining = {}".format(lamb_remaining)
        if b <= lamb_remaining:
            num_persons = num_persons + 1 
            temp.append(b)
            lamb_remaining = lamb_remaining - b
    return num_persons, temp


i =  143  
print("Calling stingy with {}".format(i))
payout1, temp = stingy(i)
print("Possible stingy payout {} {}".format(payout1, temp))
print("Calling generous with {}".format(i))
payout2, temp = generous(i)
print("Possible generous payout {} {}".format(payout2,temp))
print("difference = {}".format(payout1-payout2))
