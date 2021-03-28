# takes in a list and if an element occurs more than n times, removes all occurences of that element from the list

def remove_excess(data, n):
    to_remove = []
    final_data = []
    for i in data:
        if data.count(i) > n:
            to_remove.append(i)
    for index in range(len(data)):
        if(data[index] in to_remove):
            continue
        else:
            final_data.append(data[index])
    return final_data

print(remove_excess([1,2,2,2,2,3,4,5,6,7,8], 3))

# returns [1, 3, 4, 5, 6, 7, 8]
