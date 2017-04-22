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
import copy

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

def print_dictionary(d):
    for k in d.keys():
        print(k," -> " , d[k])

def depth_first_search(all_words_hash_map, currlist, visited_nodes, curr_word, end_word, allpaths):
    keylist =  get_all_possible_hash_words(curr_word)
    currlist.append(curr_word)
    print("curlist in the begininging = {}".format(currlist))
    print("currentword = %s"%curr_word)
    for key in keylist:
        transformedwordlist = all_words_hash_map[key]
        print("key = {} list = {}".format(key,transformedwordlist))
        if end_word in transformedwordlist:
            print("Found end word %s"%end_word)
            currlist.append(end_word)
            templist = copy.deepcopy(currlist)
            allpaths.append(templist)
            return
    for key in keylist:
        templist = copy.deepcopy(all_words_hash_map[key])
        templist2 = copy.deepcopy(templist)
        for word in templist:
            if word in currlist:
                templist2.remove(word)
                print("templist after word removal = {}".format(templist2))
        templist = templist2
        for word in templist:
            print("Now about to recurse with word %s"%word)
            depth_first_search(all_words_hash_map, currlist, visited_nodes, word, end_word, allpaths)
            print("curlist after recursion = {}".format(currlist))
            if end_word in currlist:
                currlist.remove(end_word)
            currlist.remove(word)


test_words = [ 'dat', 'cat', 'hat', 'hot', 'hog', 'dog' ]

words = {
                "cat", "rat", "hat", "sag", "bag", "bug", "dog", "hog", "hot", "dot",
                "rot", "lot", "log", "cry", "pry", "fry", "fat", "fog", "pot", "fat"
        }
#print(test_words)
print(words)
print("\n")
all_words_hash_map = create_hash_map(words)
#all_words_hash_map = create_hash_map(test_words)
print_dictionary(all_words_hash_map)
#end_word = "cay"
end_word = "dog"
currlist = []
curr_word = 'cat'
#curr_word = 'bai'
visited_nodes = []
allpaths = []
print(depth_first_search(all_words_hash_map, currlist, visited_nodes, curr_word, end_word, allpaths))
#depth_first_search(all_words_hash_map, currlist, visited_nodes, curr_word, end_word, allpaths)
print("allpaths")
allpaths.sort( key=len)
shortest = len(allpaths[0])
for k in allpaths:
    if len(k) == shortest:
        print(k)



