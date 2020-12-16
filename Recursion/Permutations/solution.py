from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_rec(nums, start):
            if start >= len(nums):
                allPermutations.append(list(nums))
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permute_rec(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]

        allPermutations = list()
        permute_rec(nums, 0)
        return allPermutations


sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))
