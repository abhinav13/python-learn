from collections import defaultdict
from collections import OrderedDict

def create_pairs(array1, array2 ):

    ret_val = [ (x, y) for x in array1 for y in array2 ]
    return ret_val


array1 = [1, 2, 4]
array2 = [1, 9, 13]

mergedlist = create_pairs(array1, array2)

d = defaultdict(list)

for el in mergedlist:
    d[sum(el)].append(el)

h = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

print(d)
print(h)
