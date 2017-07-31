
def foo(s, i, j):

    if len(s) < 1:
        return 0
    if len(s) == 1:
        return 1
    if i == j:
        return 1
    max_len = 0
    if s[i] == s[j] and i+1 == j:
        return 2
    if s[i] == s[j]:
        max_len = 2 + foo(s,i+1,j-1)
    else:
        max_len = max(foo(s, i+1, j), foo(s, i, j-1))

    return max_len


s = 'geeksaaageeks'
i = 0
j = len(s)-1
print("leng of s = {}".format(j))
m = foo(s, i, j)
print(m)
