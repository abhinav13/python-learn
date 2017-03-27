#http://www.programcreek.com/2015/07/leetcode-find-k-pairs-with-smallest-sums-java/
#LeetCode – Find K Pairs with Smallest Sums (Java)
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
# Example:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
# Return: [1,2],[1,4],[1,6]
# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

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
