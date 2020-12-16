from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedSet = sorted(set(arr))
        # print(sortedSet)
        rank = dict()
        for i, num in enumerate(sortedSet):
            rank[num] = i+1
        # print(rank)
        return [rank[num] for num in arr]


# test driver
sol = Solution()
arr = [37,12,28,9,100,56,80,5,12]
print("Input:", arr)
print("Output:", sol.arrayRankTransform(arr))