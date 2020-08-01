from typing import List
import math

# count the biggest contiguous zeros
# case 1: between 1's
# Max distance = Math.ceil(#zero/2)
# case 2: at the edge
# Max distance = #zero
def maxDistToClosest(seats: List[int]) -> int:
    maxDistance = 0
    newMaxDistance = 0
    numZeros = 0
    firstZeroIndex = -1
    for i, occupied in enumerate(seats):
        if occupied:
            # 0's at the left edge
            if firstZeroIndex == 0:
                newMaxDistance = numZeros
            # 0's in between 1's
            else:
                newMaxDistance = math.ceil(numZeros/2)
            maxDistance = max(maxDistance, newMaxDistance)
            numZeros = 0
            firstZeroIndex = -1
        else:
            numZeros += 1
            if firstZeroIndex == -1:
                firstZeroIndex = i
    # 0's at the right edge
    if numZeros != 0:
        newMaxDistance = numZeros
        maxDistance = max(maxDistance, newMaxDistance)
    return maxDistance


# Test Driver
input = [1,0,0,0,1,0,1]
print("Input:", input)
print("Output:", maxDistToClosest(input))

input = [1,0,0,0]
print("Input:", input)
print("Output:", maxDistToClosest(input))

input = [0,0,0,1,0,0,0,1,0,0]
print("Input:", input)
print("Output:", maxDistToClosest(input))

input = [1,0,0,0,0,1,0,0,0]
print("Input:", input)
print("Output:", maxDistToClosest(input))