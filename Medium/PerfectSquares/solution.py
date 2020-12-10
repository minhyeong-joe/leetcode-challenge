import math


def numSquares(n: int) -> int:
    queue = list([(n, 0)])
    visited = set([n])
    while queue:
        currentNum, depth = queue.pop(0)
        maxSqrt = math.floor(math.sqrt(currentNum))
        for i in range(maxSqrt, -1, -1):
            remainingNum = currentNum - i * i
            if remainingNum == 0:
                return depth+1
            elif remainingNum not in visited:
                queue.append((remainingNum, depth+1))


print(numSquares(12))
print(numSquares(13))
print(numSquares(61))
print(numSquares(48))
