#!/bin/python3

import sys


s = input().strip()
t = input().strip()
#k = int(input().strip())

n, k = s.split()
l = t.split()

#if n != len(l):
#    sys.exit()
powerset = []
currentset = []
def get_subset(j,k,l):
     """ This helper function returns a subset from the
         current list, if j and k are the same, then the element
         at that location is returned
     """
     ret_list = []
     if j == k:
         ret_list.append(l[j])
     else:
         for z in range(j,k+1):
             ret_list.append(l[z])
     return ret_list

for i, element in enumerate(l):
     currentset.append(element)
     powerset.append(currentset)
     for j in range(i+1, len(l)):
         for k in range(j,len(l)):
             temp = get_subset(j,k,l)
             temp.insert(0,element)
             powerset.append(temp)
     currentset = []

current_len =0
found = True
for e in powerset:
   if len(e) > 1: #only want subsets that have atleast two elements
       temp = [(e[x],e[y]) for x in range(len(e)) for y in range(x+1, len(e))]        
       for i in temp:
           num1, num2 = i
           if (int(num1) + int(num2)) % k == 0:
             found = False
       if found:
           if current_len < len(e):
               current_len = len(e)
       found = True  #Reset the flag
print(current_len)