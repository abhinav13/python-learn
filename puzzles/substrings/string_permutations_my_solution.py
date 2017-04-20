def swap(array, i, j):
    c = list(array)
    temp = c[i]
    c[i] = c[j]
    c[j] = temp
    return ''.join(c)


def _recurselistoflists(array, index):
    print(array)
    if index == len(array)-1:
        return
    # print("index = ", index)
    for i in range(index, len(array)):
        for j in range(i+1, len(array)):
            array = swap(array, i, j)
            # print("after swaping ", array)
            _recurselistoflists(array, i+1)
            # now swap back
            array = swap(array, j, i)

# a = 'ABCDEFGHIJ'
# _recurselistoflists(a, 0)
