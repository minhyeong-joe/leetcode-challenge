from typing import List


def prisonAfterNDays(cells: List[int], N: int) -> List[int]:
    # the pattern repeats every 15 days
    N = (N-1) % 14 + 1
    prev = cells
    current = list()
    for day in range(N):
        for i in range(len(prev)):
            # first and last cell is always vacant because it does not have two adjacent neighbors
            if i == 0 or i == len(prev)-1:
                current.append(0)
            # insert 0 or 1 based on neighboring cells
            else:
                isOccupied = 1 if not(prev[i-1] ^ prev[i+1]) else 0
                current.append(isOccupied)
        # after each day, set current to be prev, and new list as current
        prev = current
        # print("Day", day+1, ":", current)
        current = list()
    return prev


# test driver
cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 7
print("Input: cells =", cells, ", N =", N)
print("Output:", prisonAfterNDays(cells, N))
print()

cells = [1, 0, 0, 1, 0, 0, 1, 0]
N = 1000000000
print("Input: cells =", cells, ", N =", N)
print("Output:", prisonAfterNDays(cells, N))
print()
