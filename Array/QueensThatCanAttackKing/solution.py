from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attackable = list()
        i, j = king[0], king[1]
        # check top
        while i > 0:
            i -= 1
            # print([i,j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        i = king[0]
        # print(attackable)
        # check top-right
        while i > 0 and j < 7:
            i -= 1
            j += 1
            # print([i,j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        i, j = king[0], king[1]
        # print(attackable)
        # check right
        while j < 7:
            j += 1
            # print([i, j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        j = king[1]
        # print(attackable)
        # check bottom-right
        while i < 7 and j < 7:
            i += 1
            j += 1
            # print([i, j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        i, j = king[0], king[1]
        # print(attackable)
        # check bottom
        while i < 7:
            i += 1
            # print([i,j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        i = king[0]
        # print(attackable)
        # check bottom-left
        while i < 7 and j > 0:
            i += 1
            j -= 1
            # print([i, j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        i, j = king[0], king[1]
        # print(attackable)
        # check left
        while j > 0:
            j -= 1
            # print([i, j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        j = king[1]
        # print(attackable)
        # check top-left
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            # print([i, j])
            if [i, j] in queens:
                attackable.append([i, j])
                break
        i, j = king[0], king[1]
        # print(attackable)

        return attackable


# test driver
sol = Solution()
queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]
print("Output:", sol.queensAttacktheKing(queens, king))