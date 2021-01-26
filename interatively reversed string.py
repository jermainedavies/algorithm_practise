def reverse(list):
    reversed = []
    index = len(list)-1
    for i in range(len(list)):
        reversed += list[index]
        index -=1
    return reversed

print(reverse(["c","h","o","c","o","l","a","t","e"])) # returns "etalocohc"
