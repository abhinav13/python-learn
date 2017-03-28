from collections import OrderedDict
from collections import defaultdict

l = [ 1,1,2,14,56,45,13,2,1,2,3,3,3,3,3,45,56,56,56]

d = defaultdict(int)

for el in l:
    d[el] += 1

print(d)

e = defaultdict(list)
for k,v in d.items():
   e[v].append(k)
   e[v].sort()

o = OrderedDict(sorted(e.items(),reverse=True))
for i,v in o.items():
    print v
