def isPrime(number):
    for i in range(2, int(number/2)):
        if number%i == 0:
            return False
    return True
