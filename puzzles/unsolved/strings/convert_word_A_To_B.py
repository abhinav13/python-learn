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

def breadth_first_search(global_hash, current_path, visited_nodes, curr_word, end_word):
    print("-----------------------------------")
    print("current word {} currentpath {} ".format(curr_word, current_path))
    all_possible_words = get_all_possible_hash_words(curr_word)
    print ("all_possible_words {}".format(all_possible_words))
    # for word in all_possible_words:
    #     print("word = %s" % word)
        #else we pick the next word from the global hash list and call ourselves again
    #     else:
    current_path.append(curr_word)

    visited_nodes.append(curr_word)
    print("current path after append {}".format(current_path))
    for w in all_possible_words:
        current_word_list = global_hash[w]
        if end_word in current_word_list:   # we found it
            print("Found it!!")
            current_path.append(end_word)
            print("current path before returning when found {}".format(current_path))
            return
        print("keyword is %s" % w)
        print("current_word_list for keyword {s} is {l}".format(s=w, l=current_word_list))
        # remove the current_word
        # current_word_list.remove(curr_word)
        for dictionary_word in current_word_list:
            print("dictionary word %s" % dictionary_word)
            if dictionary_word not in visited_nodes:
                print("current path before calling {}".format(current_path))
                breadth_first_search(global_hash, current_path, visited_nodes, dictionary_word, end_word)
                if end_word not in current_path and dictionary_word in current_path: # search was unsuccessful
                    # remove the current word from the current_path and move
                    # on
                    current_path.remove(dictionary_word)
                    print("current path after removal {}".format(current_path))
            if end_word in current_path:
               return #we found it
    return

def depth_first_search(global_hash, current_path, visited_nodes, start_word, end_word, allpaths):
    print("-----------------------------------")
    print("current word {} currentpath {} ".format(start_word, current_path))
    all_possible_words = get_all_possible_hash_words(start_word)
    print ("all_possible_words {}".format(all_possible_words))
    current_path.append(start_word)
    print("current path after append {}".format(current_path))
    for w in all_possible_words:
        current_word_list = global_hash[w]
        if end_word in current_word_list:
            current_path.append(end_word)
            print("current path before returning when found {}".format(current_path))
            temp = []
            temp = copy.deepcopy(current_path)
            allpaths.append(temp)
            return
    #we did not find the end word in the current possible word list
    for w in all_possible_words:
        current_word_list = global_hash[w]
        print("current word list", current_word_list)
        if w not in visited_nodes:
            visited_nodes.append(w)
            for possible_word in current_word_list:
                if possible_word != start_word: # dont call yourself again
                    print("possible word {}".format(possible_word))
                    depth_first_search(global_hash, current_path, visited_nodes, possible_word, end_word, allpaths)
                    # if end_word in current_path:
                    #    allpaths.append(current_path)
                    if possible_word in current_path:
                        print("removing possible word from path %s"%possible_word)
                        current_path.remove(possible_word)
        else:
            print("skipped key %s" % w)
    #This was worthless remove start word
    if start_word in current_path and end_word not in current_path:
        print("removing word %s" % start_word)
        current_path.remove(start_word)
    print("reurning at the end of the function with start word %s" %start_word)


test_words = [ 'cay', 'bay', 'bai' ]

words = {
                "cat", "rat", "hat", "sag", "bag", "bug", "dog", "hog", "hot", "dot",
                "rot", "lot", "log", "cry", "pry", "fry", "fat", "fog", "pot", "fat"
        }
#print(test_words)
#print(words)
print("\n")
all_words_hash_map = create_hash_map(words)
#all_words_hash_map = create_hash_map(test_words)
print(all_words_hash_map)
#end_word = "cay"
end_word = "dog"
currlist = []
curr_word = 'cat'
#curr_word = 'bai'
visited_nodes = []
allpaths = []
# breadth_first_search(all_words_hash_map, currlist, visited_nodes, curr_word,
# end_word, allpaths)
depth_first_search(all_words_hash_map, currlist, visited_nodes, curr_word, end_word, allpaths)
print("Found path")
print(currlist)
print("allpaths")
print(allpaths)
