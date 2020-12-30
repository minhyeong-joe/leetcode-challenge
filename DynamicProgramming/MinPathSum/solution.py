def minPathSum(grid):
    # init dynamic programming table
    dp = [[None for _ in grid[0]] for _ in grid]
    dp[0][0] = grid[0][0]
    for i in range(1, len(dp)):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, len(dp[0])):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    print("initial dp:", dp)
    # fill in dp table
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            minCostSoFar = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            dp[i][j] = minCostSoFar + grid[i][j]
    print("after fill-in:", dp)
    return dp[-1][-1]


grid = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minPathSum(grid))
