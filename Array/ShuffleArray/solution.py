from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = list()
        for x in range(n):
            result.append(nums[x])
            result.append(nums[x+n])
        return result


# test driver
sol = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(sol.shuffle(nums, n))