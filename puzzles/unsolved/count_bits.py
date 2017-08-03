

def count_bits(num):

    mask = 1
    count = 0
    while num > 0:
        if num & mask > 0:
            count = count + 1
        num = num >> 1
    return count


print("input = 2 coun_bits = {}".format(count_bits(2)))
print("input = 15 coun_bits = {}".format(count_bits(15)))
print("input = 0 coun_bits = {}".format(count_bits(0)))
print("input = 63 coun_bits = {}".format(count_bits(63)))

