from typing import List

# Recursively find all combinations (ie. brute force) is not efficient


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # recursively find all combinations
        # def combinationOfTwo(arr, start=0, comb=[]):
        #     if len(comb) == 2:
        #         combinations.append(list(comb))
        #         return
        #     for i in range(start, len(arr)):
        #         comb.append(i)
        #         combinationOfTwo(arr, i+1, comb)
        #         comb.pop()

        # find height given two indices for containers
        def waterContainer(arr, left, right):
            height = min(arr[left], arr[right])
            width = right-left
            return height*width

        # combinations = list()
        result = 0
        # combinationOfTwo(height)
        # for left, right in combinations:
        #     result = max(result, waterContainer(height, left, right))

        left = 0
        right = len(height)-1
        while left < right:
            result = max(result, waterContainer(height, left, right))
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
        return result


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
