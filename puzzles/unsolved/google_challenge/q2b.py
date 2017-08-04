

def solveit(l):

    current_op = False # False  is subtract, 1 is add

    l_sum_of_radius = []
    ret_list = []
    # calculate radius difference
    i = l[0]
    for j in l[1:]:
        l_sum_of_radius.append(j-i)
        i = j

    next_sum = l_sum_of_radius[0]

    temp_list = []
    for second_sum in l_sum_of_radius[1:]:
        if current_op:
            next_sum = next_sum + second_sum
            temp_list.append(next_sum)
            current_op = False
        else:
            next_sum = next_sum - second_sum
            temp_list.append(next_sum)
            current_op = True
        if next_sum < 0:
           return [-1, -1]
    if current_op: #last op was an add
        x = next_sum * 2
        ret_list.append(x)
        ret_list.append(1)
    else:
        ret_list.append(x)
        ret_list.append(3)
    return ret_list


l = [4,30,50]

print(solveit(l))
l = [4,17,50]
print(solveit(l))
