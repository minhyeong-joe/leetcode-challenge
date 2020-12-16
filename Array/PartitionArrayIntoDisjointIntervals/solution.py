from typing import List

def partitionDisjoint(A: List[int]) -> int:
    rightIndex = 1
    leftHighest = A[0]
    highest = A[0]
    for i in range(1, len(A)):
        # if higher value, update the highest
        if A[i] >= leftHighest:
            highest = max(highest, A[i])
        # if lower values, then they belong to the left subarray (the highest so far is now the highest on the left subarray)
        else:
            rightIndex = i + 1
            leftHighest = highest
    return rightIndex

# test driver
input = [5,0,3,8,6]
print("Input:", input)
print("Output:", partitionDisjoint(input))
print()

input = [1,1,1,0,6,12]
print("Input:", input)
print("Output:", partitionDisjoint(input))
print()