# Coin Change

[Leetcode Link](https://leetcode.com/problems/coin-change/)

## Problem:

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Example:

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

```
Input: coins = [2], amount = 3
Output: -1
```

```
Input: coins = [1], amount = 0
Output: 0
```

```
Input: coins = [1], amount = 1
Output: 1
```

## Note:

- 1 <= coins.length <= 12
- 1 <= coins[i] <= 231 - 1
- 0 <= amount <= 104
