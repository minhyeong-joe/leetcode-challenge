# Regular Expression Matching

[Leetcode Link](https://leetcode.com/problems/regular-expression-matching/)

## Problem:

Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​
- `'*'` Matches zero or more of the preceding element.
  The matching should cover the _entire_ input string (not partial).

## Example:

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

```
Input: s = "mississippi", p = "mis*is*p*."
Output: false
```

## Note:

- 0 <= s.length <= 20
- 0 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '\*'.
- It is guaranteed for each appearance of the character '\*', there will be a previous valid character to match.
