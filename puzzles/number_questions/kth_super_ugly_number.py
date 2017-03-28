#
#http://www.programcreek.com/2014/05/leetcode-super-ugly-number-java/Write a program to find the nth super ugly number.
#
#Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.bit_length
#Note:
#    (1) 1 is a super ugly number for any given primes.
#    (2) The given numbers in primes are in ascending order.
#    (3) 0 < k < = 100, 0 < n < = 106, 0 < primes[i] < 1000.


def get_primefactors(number):
    l = []
    for i in range(1,int(number/2)):
        prime_factos = [2,3,5,7,11,13,17,19,23,29,31]
        # for each number in primefactor
        # if it divides the number without remainder, keep doing it
        # divide the number, then replace the mantissa with the remainder
        # if the new matissai not divisible by the current number, get new
        # number from the list. Keep doing it till the remainder is 0
