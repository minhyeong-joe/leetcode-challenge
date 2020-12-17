def unboundedKnapsack(weights, values, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i][j-weights[i-1]]+values[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[-1][-1]


weights = [1, 2, 3, 5]
values = [1, 4, 7, 10]
capacity = 8
print(unboundedKnapsack(weights, values, capacity))
