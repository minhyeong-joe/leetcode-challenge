def uniqueTwoSum(nums, target):
    numPairs = 0
    # sort array
    nums.sort()
    # two pointers from left-end and right-end
    left = 0
    right = len(nums)-1
    while left < right:
        # skip the same numbers (finding UNIQUE pairs)
        while left >= 1 and nums[left] == nums[left-1]:
            left += 1
            if left >= len(nums):
                break
        while right < len(nums)-1 and nums[right] == nums[right+1]:
            right -= 1
            if right < 0:
                break
        if left >= right:
            break
        if nums[left] + nums[right] == target:
            numPairs += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return numPairs


# simple test case
nums = [1, 1, 2, 3, 4, 4, 43, 45, 45, 46, 46]
target = 47
print(uniqueTwoSum(nums, target))

# all dups
nums = [1, 1, 1, 1, 1, 1, 1]
target = 2
print(uniqueTwoSum(nums, target))

# no two sum to target
nums = [2, 3, 6, 2, 3]
target = 7
print(uniqueTwoSum(nums, target))

# unique
nums = [1, 5, 1, 5]
target = 6
print(uniqueTwoSum(nums, target))
