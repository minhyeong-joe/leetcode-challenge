from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find all 'O's on border
        notCaptured = list()
        for i in range(len(board)):
            # first or last row
            if i == 0 or i == len(board)-1:
                for j in range(len(board[i])):
                    if board[i][j] == 'O':
                        notCaptured.append((i,j))
            # other rows
            else:
                for j in [0, len(board[i])-1]:
                    if board[i][j] == 'O':
                        notCaptured.append((i,j))
        # print(notCaptured)
        # for each O on border, do DFS and mark those 'O's as NOT SURROUNDED
        while notCaptured:
            current = notCaptured.pop()
            i = current[0]
            j = current[1]
            board[i][j] = 'N'
            # print("Current Coordinate:", current)
            # check UP
            if i-1 >=0 and board[i-1][j] == 'O':
                notCaptured.append((i-1, j))
            # check RIGHT
            if j+1 < len(board[i]) and board[i][j+1] == 'O':
                notCaptured.append((i, j+1))
            # check DOWN
            if i+1 < len(board) and board[i+1][j] == 'O':
                notCaptured.append((i+1, j))
            # check LEFT
            if j-1 >= 0 and board[i][j-1] == 'O':
                notCaptured.append((i, j-1))

            # print("DFS stack:", notCaptured)

        # for row in board:
        #     print(row)

        # now flip 'O's to 'X's, and 'N's back to 'O's
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'



# test driver
sol = Solution()
board = [['O','X','X','X','X','X'],
         ['X','O','O','X','O','X'],
         ['X','X','O','X','O','O'],
         ['X','O','X','X','O','X'],
         ['O','O','X','X','X','X']]
print("Input:")
for row in board:
    print(row)

sol.solve(board)

print("Output:")
for row in board:
    print(row)