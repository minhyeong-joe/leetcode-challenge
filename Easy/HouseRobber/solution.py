from typing import List

def rob(nums: List[int]) -> int:
    robbedSums = [0]*len(nums)
    for i, robbed in enumerate(nums):
        if i-2 < 0:
            robbedSums[i] = robbed
        else:
            prevMax = max(robbedSums[i-2], robbedSums[i-3]) if i-3 >= 0 else robbedSums[i-2]
            robbedSums[i] = robbed + prevMax
    return max(robbedSums) if robbedSums else 0


# test driver
nums = [2, 1, 1, 2]
print("Input: nums =", nums)
print("Output:", rob(nums))
print()

nums = [2,7,9,3,1]
print("Input: nums =", nums)
print("Output:", rob(nums))
print()
