def findmax_sum(l, index):

    if len(l) -1 == index:
        return l[index]
    current_elem = l[index]

    max_sum = max(current_elem, max(current_elem + findmax_sum(l, index+1),
                                    findmax_sum(l, index + 1)))
    return max_sum


l=[2,-8]
print(l)
print(findmax_sum(l,0))

l=[2,8]

print(l)
print(findmax_sum(l,0))

l=[2, -8, 3]
print(l)
print(findmax_sum(l,0))
