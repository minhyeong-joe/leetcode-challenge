
# Minimum Number of Steps to Make Two Strings Anagram
[Leetcode Link](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)

## Problem:

Given two equal-size strings `s` and `t`. In one step you can choose **any character** of `t` and replace it with **another character**.

Return *the minimum number of steps* to make `t` an anagram of `s`.

An **Anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

## Example:

```
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```
```
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```
```
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
```
```
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
```
```
Input: s = "friend", t = "family"
Output: 4
```

## Note:

- `1 <= s.length <= 50000`
- `s.length == t.length`
- `s` and `t` contain lower-case English letters only.