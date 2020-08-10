from typing import List
import math


def majorityElement(nums: List[int]) -> int:
    numCounter = dict()
    for num in nums:
        numCounter[num] = numCounter.get(num, 0) + 1
    for k, v in numCounter.items():
        if v > math.floor(len(nums)/2):
            return k
    return None


# test driver
input = [3, 2, 3]
print("Input:", input)
print("Output:", majorityElement(input))
print()

input = [2, 2, 1, 1, 1, 2, 2]
print("Input:", input)
print("Output:", majorityElement(input))
print()
