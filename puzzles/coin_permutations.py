import copy


def coins(target, current_list, listofcoinscombos, validcoinlist):

    if sum(current_list) == target:
        listofcoinscombos.append(copy.deepcopy(current_list))
        return
    elif sum(current_list) > target:
        return

    for coin in validcoinlist:
        current_list.append(coin)
        ret_val = coins(target, current_list, listofcoinscombos, validcoinlist)
        current_list.pop()


validcoinlist = [1, 2]
current_list = []
listofcoinscombos = []
target = 3

print(listofcoinscombos)
coins(target, current_list, listofcoinscombos, validcoinlist)
print(listofcoinscombos)
validcoinlist = [2, 3, 5]
current_list = []
listofcoinscombos = []
target = 17

coins(target, current_list, listofcoinscombos, validcoinlist)
print(listofcoinscombos)
