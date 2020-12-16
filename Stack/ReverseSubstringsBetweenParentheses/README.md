
# Reverse Substrings Between Each Pair of Parentheses
[Leetcode Link](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

## Problem:

You are given a string `s` that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should **not** contain any brackets.

## Example:

```
Input: s = "(abcd)"
Output: "dcba"
```
```
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
```
```
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
```
```
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
```

## Note:

- `0 <= s.length <= 2000`
- `s` only contains lower case English characters and parentheses.
- It's guaranteed that all parentheses are balanced.