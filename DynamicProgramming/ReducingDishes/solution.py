from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_coef = 0
        # first sort the satisfaction, so that it is easier to remove the dishes with negative likes
        # and if chef can cook in any order, it is best to cook the most-liked towards end (greater multiplication factor)
        satisfaction.sort()
        # similar to Dynamic Programming, check max like-time coefficient with each negative dishes removed from 1-n
        for start in range(0, len(satisfaction)):
            dish = 1
            current = 0
            for order in range(start, len(satisfaction)):
                current += satisfaction[order] * dish
                dish += 1
            # print(start, "-", len(satisfaction), ":", current)
            max_coef = max(max_coef, current)
            # print("Max so far:", max_coef)

        return max_coef

# test driver
sol = Solution()
satisfaction = [-1,-8,0,5,-9]
print("Input: satisfaction =", satisfaction)
print("Output:", sol.maxSatisfaction(satisfaction))