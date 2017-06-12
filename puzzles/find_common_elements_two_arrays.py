a = [2, 5, 7, 8]
b = [1, 3, 5, 7]
print("a={}, b={}".format(a, b))
next_compare = []
i = 0
j = 0

cc = a
current_index = i
next_compare.append(b)
next_compare.append(j)
common_elements = []

while i < len(b) and j < len(a):
    if a[j] == b[i]:
        common_elements.append(b[i])
        i = i+1
        j = j+1
    elif a[j] < b[i]:
        j = j+1
    elif a[j] > b[i]:
        i = i+1

print("Common elements {}".format(common_elements))
