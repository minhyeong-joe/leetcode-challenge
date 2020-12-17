def knapsack(weights, values, W):
    dp = [[0 for _ in range(W+1)] for _ in range(len(weights)+1)]
    # print(dp)
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1]
                               [j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[-1][-1]


weights = [4, 5, 2, 3]
values = [5, 3, 2, 4]
W = 7
print(knapsack(weights, values, W))
