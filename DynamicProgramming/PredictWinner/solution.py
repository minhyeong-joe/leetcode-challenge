from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.minMax(nums, 0, len(nums)-1, 1)
        return score >= 0


    def minMax(self, nums: List[int], start, end, turn = 1) -> int:
        # print(nums[start:end+1])
        if start == end:
            # print("base case:", turn*nums[start])
            return turn * nums[start]
        pickLeft = turn * nums[start] + self.minMax(nums, start+1, end, -turn)
        # print("left:", pickLeft)
        pickRight = turn * nums[end] + self.minMax(nums, start, end-1, -turn)
        # print("right:", pickRight)
        return turn * max(turn * pickLeft, turn * pickRight)
        



# test driver
sol = Solution()
nums = [1, 5, 233, 7]
print("Output:", sol.PredictTheWinner(nums))