def is_valid(s):
    openers = ["(","{","["]
    closers = [")","}","]"]
    bracket_stack = []

    if len(s) % 2 != 0:
        return False
    if s[0] in closers:
        return False

    for i in range(len(s)):
        if s[i] in openers:
            bracket_stack.append(s[i])
        elif s[i] in closers:
            bracket_stack.append(s[i])
            if bracket_stack[0] in closers:
                return False
            if closers.index(bracket_stack[-1]) == openers.index(bracket_stack[-2]):
                for i in range(2):
                    bracket_stack.pop()
            else:
                return False

    if bracket_stack == []:
        return True
    return False



print(is_valid("()[]{}")) #True
print(is_valid("(]")) #False
print(is_valid("{[]}")) # True
print(is_valid("([)]")) # False
print(is_valid("(){}}{")) # False
