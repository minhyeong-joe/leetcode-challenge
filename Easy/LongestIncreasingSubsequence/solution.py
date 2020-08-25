from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        curLength = 1
        maxLength = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                # print(nums[i], "is greater than", nums[i-1])
                curLength += 1
                # print("curLength:", curLength)
            else:
                curLength = 1
            maxLength = max(curLength, maxLength)
            # print("maxLength:", maxLength)
        return maxLength


# test driver
sol = Solution()
arr = [1,3,5,4,7]
print("Input:", arr)
print("Output:", sol.findLengthOfLCIS(arr))