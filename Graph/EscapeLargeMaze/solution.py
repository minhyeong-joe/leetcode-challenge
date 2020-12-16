from typing import List

# test size is reduced to 10 x 10 grid for visual debugging
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        N = 10
        # queue for BFS
        queue = list()
        visited = set()
        queue.append(source)
        while queue:
            # print("queue:", queue)
            # print("visited:", visited)
            currentCoord = queue.pop(0)
            if currentCoord == target:
                return True
            visited.add(tuple(currentCoord))
            # get four neighboring coordinates and add to queue if not visited and is valid (not blocked and not outside boundary)
            if currentCoord[0]-1 >= 0 and (currentCoord[0]-1,currentCoord[1]) not in visited and [currentCoord[0]-1,currentCoord[1]] not in blocked:
                queue.append([currentCoord[0]-1, currentCoord[1]])
            if currentCoord[0]+1 < N and (currentCoord[0]+1, currentCoord[1]) not in visited and [currentCoord[0]+1, currentCoord[1]] not in blocked:
                queue.append([currentCoord[0]+1, currentCoord[1]])
            if currentCoord[1]-1 >= 0 and (currentCoord[0], currentCoord[1]-1) not in visited and [currentCoord[0], currentCoord[1]-1] not in blocked:
                queue.append([currentCoord[0], currentCoord[1]-1])
            if currentCoord[1]+1 < N and (currentCoord[0], currentCoord[1]+1) not in visited and [currentCoord[0], currentCoord[1]+1] not in blocked:
                queue.append([currentCoord[0], currentCoord[1]+1])
            
        return False


# test driver
sol = Solution()
blocked = []
source = [0,0]
target = [9, 9]
print("Output:", sol.isEscapePossible(blocked, source, target))