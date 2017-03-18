# http://www.programcreek.com/2014/06/leetcode-substring-with-concatenation-of-all-words-java/


# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s)
# in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given: s="barfoothefoobarman" & words=["foo", "bar"], return [0,9].

def remove_word(a, word):
    ret_val = []
    for el in a:
        if word != a:
            ret_val.append(el)
    return ret_val

def does_substring_exist(s, current_index, words):
    length = len(words[0]) 
    w = s[current_index:length+1]   
    for el in words:
        if el == w: # found one, so we found one word that matches, now we need to see if the remaining elements are in
                    # remaining string
        print("Found a potential match")
        remainder = s[(current_index+len(el)):((len(words)-1)*length)]
        print("remainder = {r}".format(r=remainder))
        search_words = remove_word(words, el)
        found = True
        for el in search_words:
            if el not in remainder:
                print("Did not find {w} in string {r}".format(w=el,r=remainder))
                found = False
                break
        if not found:
            print("returning false")
            return False
        else:
            print("Returning true")
            return True

s="barfoothefoobarman" 
words=["foo", "bar"]
answer = []
print("starting")
for i in range(0,len(s)):
    if does_substring_exist(s, i, words):
        answer.append(i)

print(answer)
