def selection_sort(to_sort):
    sorted = False
    min = to_sort[0]

    for i in to_sort:
        if i < min:
            min = i

    while not sorted:
        sorted = True
        for i in range(len(to_sort)-1):
            if to_sort[i] > to_sort[i+1]:
                to_sort[i],to_sort[i+1] = to_sort[i+1],to_sort[i]
                sorted = False

    return to_sort

print(selection_sort([8,12,29,5,20,13,7])) # returns [5, 7, 8, 12, 13, 20, 29]
