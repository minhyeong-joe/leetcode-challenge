from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for amt in range(1, amount+1):
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
            print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1


sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))
