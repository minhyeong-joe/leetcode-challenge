from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # mark negatives and zeros with number larger than len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1
        print("after marking useless numbers:", nums)
        # use negative to mark positive integer has appeared
        for i in range(len(nums)):
            absolute = abs(nums[i])
            if absolute <= len(nums):
                # in case of duplicate (to prevent more than one negation)
                nums[absolute-1] = -nums[absolute-1] if nums[absolute-1] > 0 else nums[absolute-1]
        print("After marking positions:", nums)
        # first positive position + 1 is the first missing positive, if none, then len(nums) + 1 is the first missing
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1


# test driver
sol = Solution()
input = [4, 0, 1, 2, 0]
print("Input:", input)
print("Output:", sol.firstMissingPositive(input))