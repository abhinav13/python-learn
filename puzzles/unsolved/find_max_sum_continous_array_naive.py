def findmax_subarray(l):

    max_sum_so_far = 0
    ret_list = []

    for i, element in enumerate(l):
        temp_sum = element
        temp_list = []
        temp_list.append(element)
        for j, sub_element in enumerate(l[i+1:]):
            #if sub_element + temp_sum > temp_sum:
            temp_sum = temp_sum + sub_element
            if max_sum_so_far < temp_sum:
                max_sum_so_far = temp_sum
                temp_list.append(sub_element)
                ret_list = temp_list
            #else:
            #    break # we saw a number addtion of this number makes the sum we have seen so fr
                      # smaller so we can bug out of this sequence
    return max_sum_so_far, ret_list


l = [2,8,-3]
print(l)
print(findmax_subarray(l))


l = [2,-8,3,-2,4,-10]
print(l)
print(findmax_subarray(l))
