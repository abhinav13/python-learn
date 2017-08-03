# http://blog.gainlo.co/index.php/2017/01/05/uber-interview-questions-permutations-array-arrays
# Following our previous posts about Uber interview questions, this week we’re going to talk about one of my favorite questions –
# permutations of an array of arrays.
#
# If you keep following our blog, I hope you can solve this problem by yourself as a lot of ideas and techniques used here are
# common. Here we go.
#
#  Permutations of an Array of Arrays
#  Given a list of array, return a list of arrays, each array is a combination of one element in each given array.
#  Let me give you an example to help you understand the question Suppose the input is [[1, 2, 3], [4], [5, 6]], the output should
#  be [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]].


def printcombos(aa, cur_index, print_array):
    if cur_index == len(aa):
        print(print_array)
        return
    else:
        current_array = aa[cur_index]
        for el in current_array:
            print_array.append(el)
            printcombos(aa, cur_index+1, print_array)
            print_array.remove(el)
    return


def dothis(array_of_arrays):
    index = 0
    print_array = []
    printcombos(array_of_arrays, index, print_array)


aa = [[1, 2, 3], [4], [5, 6]]

dothis(aa)
