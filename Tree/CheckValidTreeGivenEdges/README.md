# Check Valid Tree Given Edges

## Problem:

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## Example:

```
Input: n = 4, edges = [(0,1), (2,0), (3,2)]
Output: true
        0
      /   \
     1     2
          /
         3

Input: n = 4, edges = [(0,1), (0,2), (2,1), (0,3)]
Output: false
         0
      /  |  \
     1 - 2   3
```
