# Substrings with exactly K distinct chars

[Leetcode Link](https://leetcode.com/discuss/interview-question/370157)

## Problem:

Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.

## Example:

```
Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
```

```
Input: s = "aabab", k = 3
Output: 0
```

## Note:

- The input string consists of only lowercase English letters [a-z]
- 0 ≤ k ≤ 26
