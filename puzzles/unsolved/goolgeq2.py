
def stingy(number):
    if number == 1:
        return [1]
    if number == 0 or number < 0:
        return []
    tot = 0
    num_persons = []
    a = 1
    b = 1
    c = 0
    tot = a + b
    num_persons.append(a)
    num_persons.append(b)
    while tot < number:
        c = a + b
        tot = tot + c
        if tot < number:
            num_persons.append(c)
        a = b
        b = c
    return num_persons


def generous(number):
    if number == 1:
        return [1]
    if number == 0 or number < 0:
        return []
    tot = 0
    num_persons = []
    a = 1
    num_persons.append(a)
    while tot < number:
        b = a*2
        tot = tot + b
        if tot < number:
            num_persons.append(b)
        a = b
    return num_persons


i =  10
print("Calling stingy with {}".format(i))
payout = stingy(i)
print("sum of payouts {}".format(sum(payout)))
print("Possible stingy payout {}".format(payout))
print("Calling generous with {}".format(i))
payout = generous(i)
print("sum of payouts {}".format(sum(payout)))
print("Possible generous payout {}".format(payout))
