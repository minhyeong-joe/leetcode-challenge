def maxScore(grid):
    dp = [[None for _ in range(len(grid))] for _ in range(len(grid))]
    # top and left borders have 1 unique path, so the score is minimum of previous col or row
    for j in range(1, len(dp[0])):
        dp[0][j] = grid[0][j] if j == 1 else min(dp[0][j-1], grid[0][j])
    for i in range(1, len(dp)):
        dp[i][0] = grid[i][0] if i == 1 else min(dp[i-1][0], grid[i][0])
    # score will be based on either route is from top or left, we want to take max score out of two paths
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            fromTop = min(dp[i-1][j], grid[i][j])
            fromLeft = min(dp[i][j-1], grid[i][j])
            dp[i][j] = max(fromTop, fromLeft)
    return max(dp[-2][-1], dp[-1][-2])


print(maxScore([[1, 2, 3], [4, 5, 1]]))
print(maxScore([[8, 4, 5], [3, 2, 7], [1, 6, 9]]))
