import pdb


def AllSubsets(array, currentindex) :

    if len(array) == 1 or len(array) == 0:
        #print("currentindex equal to lenght now")
        return array
    else:
        ret_array = []
        ##print ("currentindex = ", currentindex,array)
        current_element = array[0]
        currentindex = 0
        while currentindex < len(array):
            temp_array = []
            #print("now calling Allsubsets with array ", array[currentindex+1:])
            temp_array = (AllSubsets(array[currentindex+1:],currentindex))
            #print("temparray",temp_array)
            #print("current element = currentindex=", current_element, currentindex)
            temp = []
            temp.append(current_element)
            ret_array.append(temp)
            for el in temp_array:
                #print("el = ", el)
                if type(el) is not list:
                    #print("Found a number fixing it")
                    new_list = []
                    new_list.append(el)
                    el = new_list
                if len(el)>0:
                    el.insert(0,current_element)
                    ret_array.append(el)
                #print("return array ", ret_array)
            currentindex += 1
            if currentindex  < len(array):
                current_element = array[currentindex]
                #print("current element after incrementing = ", current_element)
        #print("ret_array just before returning", ret_array, currentindex,len(array))
        return ret_array


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
j = []
print(AllSubsets(l,0))

s="something"
print(AllSubsets(list(s),0))
