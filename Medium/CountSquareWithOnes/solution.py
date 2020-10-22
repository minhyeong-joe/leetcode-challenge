from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        # max side length is bound by the shortest side of original matrix
        maxSide = min(len(matrix), len(matrix[0]))
        # print(maxSide)
        # iterate over side length 1 to max side length, check if square is all ones (all ones if sum of elements = side**2)
        for side in range(1, maxSide+1):
            # print(f'======= side length of {side} ======')
            for i in range(0, len(matrix)-side+1):
                for j in range(0, len(matrix[i])-side+1):
                    # print(f'{i}, {j}: {matrix[i][j]}')
                    # print(f'sum of Square is: {self.sumOfSquare(matrix, i, j, side)}')
                    if self.sumOfSquare(matrix, i, j, side) == side**2:
                        count += 1
        return count

    # helper function to sum up the elements in the square given left-upper corner and side length
    def sumOfSquare(self, matrix: List[List[int]], row: int, col: int, side: int) -> int:
        sum = 0
        for i in range(row, row+side):
            for j in range(col, col+side):
                sum += matrix[i][j]
        return sum


sol = Solution()
mat = [[0,1,1,1],
       [1,1,1,1],
       [0,1,1,1]]
output = sol.countSquares(mat)
print(output)

mat2 = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
output2 = sol.countSquares(mat2)
print(output2)