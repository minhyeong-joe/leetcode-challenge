from typing import List


def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    # if r and c not valid, return original list
    if len(nums)*len(nums[0]) != r*c:
        return nums
    numCol = c
    reshaped = list()
    col = list()
    # iterate over nums and decrement numCol by 1 and when numCol reaches 0, append that col list to reshaped list, and reset numCol to c
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            col.append(nums[i][j])
            numCol -= 1
            if numCol == 0:
                # reset col list for next row
                reshaped.append(col)
                col = list()
                numCol = c
    return reshaped


# test driver
nums = [[1, 2, 3], [4, 5, 6]]
r = 3
c = 2
print("Input: nums =", nums)
print("r =", r, ", c =", c)
print("Output:", matrixReshape(nums, r, c))
