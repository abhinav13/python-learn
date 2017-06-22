

def ispalindrome(s):
    if s is None:
        return False

    if len(s) == 1:
        return True

    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


test = "AAA"
print(test, ispalindrome(test))

test = "ABCD"
print(test, ispalindrome(test))

test = "SHEAEHS"
print(test, ispalindrome(test))


test = "BANANANS"

def longest_palindrome(s):
    longest = {}
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            current_string = s[i:j+1]
            print("Checking current string {}".format(current_string))
            if ispalindrome(current_string):

