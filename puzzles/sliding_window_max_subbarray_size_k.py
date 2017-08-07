
def max_subarray(array, k):
    sum_so_far = sum(array[0:k])
    print("Initial sum = {}".format(sum_so_far))
    prev_start = 0
    i = 1
    j = i+k
    while j < len(array):

        print("i= {} subarray = {}".format(i, array[i:j]))
        print("NOw comparing new sum {} to prev sum {}".format(sum(array[i:j]), sum_so_far))
        if sum(array[i:j]) > sum_so_far:
            prev_start = i
            sum_so_far = sum(array[i:j])
        j = j +1
        i = i +1
    return sum_so_far, prev_start, prev_start+k-1


l = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3

print("l = {} k = {}".format(l, k))

print(max_subarray(l, k))
