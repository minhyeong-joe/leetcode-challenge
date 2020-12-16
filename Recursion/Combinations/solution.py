from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(nums, combination):
            if len(combination) == k:
                result.append(list(combination))
                return

            for i in range(len(nums)):
                combination.append(nums[i])
                combinations(nums[i+1:], combination)
                combination.pop()

        result = list()
        combinations([num+1 for num in range(n)], [])
        return result


sol = Solution()
n = 5
k = 3
print(sol.combine(n, k))
