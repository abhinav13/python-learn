a = [[2, 'NULL', 2, 'NULL'], 
        [2, 'NULL', 2, 'NULL'], 
        ['NULL', 'NULL', 'NULL', 'NULL'], 
        ['NULL', 'NULL', 'NULL', 'NULL']]

def foo():
    for y in range(0,3):
        for x in range(0,3):
            if a[x+1][y] != 'NULL':
                if a[x+1][y] == a[x][y]:
                    a[x][y] = a[x][y]*2
                    a[x+1][y] = 'NULL'
                
                if a[x][y] == 'NULL':
                    a[x][y] = a[x+1][y]
                    a[x+1][y] = 'NULL'

print(a)
foo()
print(a)

