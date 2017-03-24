from collections import defaultdict
from collections import OrderedDict
from itertools import product


def create_pairs2(array1, array2):
    """ This is using the itertools moduels to  give
        me a cartesian product of the array
    """
    array = list()
    array.append(array1)
    array.append(array2)
    array = list(product(*array))
    return array


def create_pairs(array1, array2):
    ret_val = [(x, y) for x in array1 for y in array2]
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

# Print K elements from the Ordered dict

j = 0
k = 3
for i, el in enumerate(h):
    for element in h[el]:
        print(element)
        j = j+1
    if j == k:  # We printed the required number of elements
        break
