from typing import List
from collections import defaultdict


class Solution:
    # the main idea is that if number of connections is less than number of computers - 1, then it is not possible to form connections
    # else, find how many disjoint graphs there are, and the number of connections that needs to be modified is simply num of disjoint - 1
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        undirectedGraph = defaultdict(list)
        for a, b in connections:
            undirectedGraph[a].append(b)
            undirectedGraph[b].append(a)
        # print(undirectedGraph)
        visited = set()
        queue = list()
        numDisjoint = 0
        # visit all computers (even disjoint ones)
        for i in range(n):
            # if computer i has been visited by BFS, then do not increment number of disjoint graph
            if i not in visited:
                queue.append(i)
                # the ones in the same queue belong to the same graph group
                while queue:
                    current = queue.pop(0)
                    visited.add(current)
                    for neighbor in undirectedGraph[current]:
                        if neighbor not in visited and neighbor not in queue:
                            queue.append(neighbor)
                numDisjoint += 1
        return numDisjoint - 1


# test driver
sol = Solution()
n = 9
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [4, 5], [4, 6], [5, 6]]
print("Output:", sol.makeConnected(n, connections))
