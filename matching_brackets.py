def is_valid(s):
    if len(s) % 2 != 0:
        return False
    openers = ["(","{","["]
    closers = [")","}","]"]
    bracket_stack = []

    for i in range(len(s)):
        if s[i] in openers:
            bracket_stack.append(s[i])
        elif s[i] in closers:
            bracket_stack.append(s[i])
            if closers.index(bracket_stack[-1]) == openers.index(bracket_stack[-2]):
                for i in range(2):
                    bracket_stack.pop()


    if bracket_stack == []:
        return True
    return False



print(is_valid("()[]{}")) #True
print(is_valid("(]")) #False
print(is_valid("{[]}")) # True
