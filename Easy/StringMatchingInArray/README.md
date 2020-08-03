
# String Matching in an Array
[Leetcode Link](https://leetcode.com/problems/string-matching-in-an-array/)

## Problem:

Given an array of string words. Return all strings in words which is substring of another word in **any** order. 

String `words[i]` is substring of `words[j]`, if can be obtained removing some characters to left and/or right side of `words[j]`.

## Example:

```
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
```
```
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
```
```
Input: words = ["blue","green","bu"]
Output: []
```

## Note:

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- `words[i]` contains only lowercase English letters.
- It's guaranteed that `words[i]` will be unique.
