from typing import List

def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    # make a index sum pair list [0][0] => 0, [0][1] => 1, [1][0] => 1...
    indexSumPairs = list()
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            indexSumPairs.append((i+j, nums[i][j]))
    # sort by index sum reversed (so it starts with "bottom" of nums array)
    indexSumPairs.sort(key=lambda pair: pair[0], reverse=True)
    return [v for _,v in reversed(indexSumPairs)]
            


# test driver:
nums = [[1,2,3],[4,5,6],[7,8,9]]
print("Input: nums =", nums)
print("Output:", findDiagonalOrder(nums))

print()
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
print("Input: nums =", nums)
print("Output:", findDiagonalOrder(nums))

print()
nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
print("Input: nums =", nums)
print("Output:", findDiagonalOrder(nums))

print()
nums = [[1,2,3,4,5,6]]
print("Input: nums =", nums)
print("Output:", findDiagonalOrder(nums))