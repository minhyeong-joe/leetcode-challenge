from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sortedPoints = sorted(points, key=lambda pair: pair[0]**2+pair[1]**2)
        return sortedPoints[:K]


sol = Solution()
points = [[3, 3], [5, -1], [-2, 4], [3, 4], [1, 5], [-2, -5], [0, 8]]
K = 2
print(sol.kClosest(points, K))
