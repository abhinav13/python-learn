def match_brackets(input_str):
    stack = []
    open_br = ['[', '{', '(']
    close_br = [']', '}', ')']
    close_dict = { ']':'[',
                  '}':'{',
                  ')':'('}
    for s in input_str:
        if s in open_br:
            stack.append(s)
        elif s in close_br:
            print("found closing bracket {}".format(s))
            print("stack[len(stack)-1] = {}".format(stack[len(stack)-1]))
            if close_dict[s] == str(stack[len(stack)-1]):
                stack.pop()
        print(stack)
    if len(stack) != 0:
        return False
    return True

print(match_brackets('{[]()}'))
print(match_brackets('{ [ ( ] ) }'))
#print("Calling match_brackets with { [ ] ( ) }\
#      return value {0}".format(match_brackets("{ [ ] ( ) }")))
#print("Calling match_brackets with { [ ( ] ) }\
#      return value {0}".format(match_brackets("{ [ ( ] ) }")))
#print("Calling match_brackets with { [ }\
#      return value {0}".format(match_brackets("{ [ }")))
