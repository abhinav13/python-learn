# Given a smaller string s, find all the permutations of s in a larger string b.
# Example: b=abbc; s=acbabbccdebabcd
# (there is an optimal solution with O(B))
import copy

def make_dict(b):
    mydict = {}
    for c in b:
        if c not in mydict.keys():
            mydict[c] = 1
        else:
            mydict[c] = int(mydict[c]) + 1
    return mydict

def remove_from_dict(d, c):
    if c in d.keys():
        if d[c] == 1:
            del d[c]
        else:
            d[c] = int(d[c]) -1


def dothis(s, b):
    if s is None or b is None:
        return 0
    if len(b) > len(s):
        return 0
    chars_in_b = make_dict(b)
    count_dict = copy.deepcopy(chars_in_b)
    b_len = len(b)
    current_len = 0
    total = 0
    flag = True
    traverse = 0

    while traverse < len(s):
        if s[traverse] in count_dict.keys():
            remove_from_dict(count_dict, s[traverse])
            current_len = current_len + 1
            flag = True

        if current_len == b_len and flag and len(count_dict) == 0:
            total = total + 1
            count_dict = copy.deepcopy(chars_in_b)

        if not s[traverse] in chars_in_b.keys():
            flag = False
            current_len = 0
            count_dict = copy.deepcopy(chars_in_b)

        traverse = traverse + 1

    return total


b = 'abbc'
s = 'acbabbccdebabcd'

print("Count of b {} in s {} = {}".format(b, s, dothis(s, b)))
