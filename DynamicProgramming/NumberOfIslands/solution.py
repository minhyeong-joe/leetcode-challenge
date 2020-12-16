from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.checkIslandDFS(grid, i, j)
        return count

    def checkIslandDFS(self, grid, i, j):
        # base case
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        # check all adjacents
        self.checkIslandDFS(grid, i, j-1)   # left
        self.checkIslandDFS(grid, i, j+1)   # right
        self.checkIslandDFS(grid, i-1, j)   # top
        self.checkIslandDFS(grid, i+1, j)   # bottom


sol = Solution()
# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# print(sol.numIslands(grid))

# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
print(sol.numIslands(grid))
