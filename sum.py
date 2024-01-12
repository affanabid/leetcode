def sum_check(nums, target):
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return f'[{i}, {j}]'

    # for i,n in enumerate(nums):
    #     diff =  target - n
    #     if diff in nums
    # for i,n in enumerate(nums):
    #     print(i)
    #     print(n)
    #     print()
    numsList = {}
    for i,n in enumerate(nums):
        diff = target-n
        if diff in numsList:
            return [numsList[diff], i]
        else:
            numsList[n] = i
print(sum_check(nums=[3,2,4], target=6))