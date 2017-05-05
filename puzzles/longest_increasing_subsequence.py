l = [2, 4, 3, 1, 7, 6, 9, 8]
print(l)
d = {}
for item in l:
    d[item] = 1

print(d)

for i in range(1, len(l)):
    potential = []
    potential.append(d[l[i]])
    for j in range(0, i):
        print("Now comparing {} {}".format(l[j],l[i]))
        if l[j] < l[i]:
            potential.append(int(d[l[i]])+int(d[l[j]]))
    d[l[i]] = max(potential)

print("Solution {}".format(d))
print("max length of string")
print(max(d.items(), key=lambda k: k[1]))
