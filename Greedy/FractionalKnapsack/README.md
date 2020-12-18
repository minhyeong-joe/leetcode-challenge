# Fractional Knapsack

## Problem:

Given `weights`: list of weights where `weights[i]` represents the weight of `i-th` item,
`values` : list of values where `values[i]` represents the value of `i-th` item,
and `capacity`, total weight available,
Find the maximum values that can be achieved within the limit of total weight.

**Unlike, 0-1 Knapsack Problem, a fraction/portion of an item can be used**

## Example:

```
weights = [1,2,3]
values = [6,10,12]
capacity = 5

Output: 24
Explanation: Whole of first two items and 2/3 of the last item
             weight = 1+2+(2/3)*3 = 5
             value = 6+10+(2/3)*12 = 24
```

## Note:
