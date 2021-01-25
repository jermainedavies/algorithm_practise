def searchInsert(nums, target):

    if target in nums:
        return nums.index(target)

    stack1 = []
    stack2 = []

    for num in nums:
        if num < target:
            stack1.append(num)
        else:
            stack2.append(num)

    stack1.append(target)
    stack1 += stack2

    return stack1.index(target)
