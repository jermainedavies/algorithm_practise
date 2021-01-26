def count_common_ints(list1,list2):
    counter = 0
    clean_list1 = []
    for i in list1:
        if i not in clean_list1:
            clean_list1.append(i)
    print(clean_list1)
    for i in clean_list1:
        if i in list2:
            counter += 1
    return counter

print(count_common_ints([3, 7, 3, -1, 2, 3, 7, 2, 15, 15],[-5, 15, 2, -1, 7, 15, 36])) # returns 4
