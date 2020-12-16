# Minimum Add to Make Parentheses Valid

## Problem:

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

- It is the empty string, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

## Example:

```
Input: "())"
Output: 1

Input: "((("
Output: 3

Input: "()"
Output: 0

Input: "()))(("
Output: 4
```

## Note:

1. S.length <= 1000
2. S only consists of '(' and ')' characters.

## Solution:

Use stack to check parentheses balance.

If `(`, then put into stack,

If `)` and stack has `(`, then pop `(` to indicate that they are balanced,

but if `)` and stack is empty, then add minimum parentheses needed.

At the end, return the size of stack + minimum parentheses needed.