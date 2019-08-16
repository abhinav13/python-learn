def isfloat(value):
      try:
        float(value)
        return True
      except ValueError:
        return False



list=[]
with open("inputnumbers.txt") as f:
    for line in f:
        if isfloat(line):
            list.append(float(line.strip()))
print( sorted(list) )#prints sorted list in ascending order
