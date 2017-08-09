def powerset(l ):

    if len(l) == 1:
        return l
    print("l = {} ".format(l))
    el = l[0]
    tempset = powerset(l[1:] )

    ret_list = []
    for element in tempset:
        ret_list.append(element)
        ret_list.append(int(str(el)+str(element)))
    ret_list.append(el)
    return ret_list



def ksub(l, k):
    allsubseq = powerset(l)
    numseq = 0
    for el in allsubseq:
        tot = 0
        l = [ int(x) for x in str(el) ]
        print(l)
        for i in l:
            tot = tot + i
        if tot%k == 0:
            numseq = numseq + 1
    return numseq

l = [2, 3, 4]
print(l)
print("um of ksubseq = {}".format(ksub(l, 5)))
