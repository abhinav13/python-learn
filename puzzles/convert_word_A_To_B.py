# http://prismoskills.appspot.com/lessons/Dynamic_Programming/Chapter_24_-_Convert_A_to_B_using_dictionary.jsp
# Problem: Given a dictionary of words and two words A and B, find the minimum path required to convert A to B.
# Only one character can be changed at a time while going from A to B and every word thus formed must be a valid dictionary word.

# Example:
#    If dictionary = {
#                "cat", "rat", "hat", "sag", "bag", "bug", "dog", "hog", "hot", "dot",
#                "rot", "lot", "log", "cry", "pry", "fry", "fat", "fog", "pot", "fat"
#            }
#    A = "cat",
#    B = "dog",
#    then shortest path from A to B should be printed as:
#        cat->hat->hot->dot->dog
#        Note: There may be longer paths like cat->rat->fat->hat->hot->dot->dog,
#        but those are not required to be printed.

from collections import defaultdict


def create_hash_map(d):
    mydict = defaultdict(list)

    #now build the hash-map
    for word in d:
        for i,c in enumerate(word):
            l = list(word)
            l[i] = str(i)
            mydict[''.join(l)].append(word)  #This creteas a hashmap of of e.g. l[0at] = cat
    return mydict

def get_all_possible_hash_words(word):
    ret_val = []
    for i,c in enumerate(word):
        l = list(word)
        l[i] = str(i)
        ret_val.append("".join(l))
          #This creteas a hashmap of of e.g. l[0at] = cat
    return ret_val



words = {
                "cat", "rat", "hat", "sag", "bag", "bug", "dog", "hog", "hot", "dot",
                "rot", "lot", "log", "cry", "pry", "fry", "fat", "fog", "pot", "fat"
        }
print(words)
all_words_hash_map = create_hash_map(words)
end_word = "dog"
current_list = []
temp_list = []
for el in words:
    wordmap = get_all_possible_hash_words(el)
    for el in worldmap:
        #look this word in global hash map dictionary
        #if the global hash map has no other words that this word can be translated to by substituting
        # single char, then we have reached a dead end, if not then we need to traverse the list we just got
        if len(all_words_hash_map[el]) == 1 and all_words_hash_map[el] != end_word:
            temp_list = []
        if end_word in all_words_hash_map[el]:  
            current_list.append(el)
            current_list.append(end_word)
            print("Found path ", current_list)

