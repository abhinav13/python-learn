

def fib(number):

    n =  1
    l = [0,1]
    if number < 2:
        return l
    prev1 = 0
    prev2 = 1
    while n < number:
        n = prev1 + prev2
        prev1 = prev2
        prev2 = n
        l.append(n)
    return l


print(fib(4))
