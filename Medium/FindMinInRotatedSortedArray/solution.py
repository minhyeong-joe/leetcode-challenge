from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = i+1 if i < len(nums)-1 else 0
            if nums[i] >= nums[j]:
                return nums[j]



# test driver
sol = Solution()
nums = [3,4,5,1,2]
print("Input:", nums)
print("Output:", sol.findMin(nums))