l = [5,50, 50]
print("input ",l)
o =  []
ret_string = ""
for i,e in enumerate(l):
    o.append(str(e))
o.sort()

for elm in reversed(o):
    ret_string = ret_string+elm

print(ret_string)
