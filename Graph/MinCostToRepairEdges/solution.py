from collections import defaultdict
import queue


def updateCost(arr, key, val):
    return [(k, v) if v != val else (key, val) for (k, v) in arr]


def minCostRepair(n, edges, edgesToRepair):
    # create edge lists associated with cost
    edgeList = defaultdict(list)
    for a, b in edges:
        edgeList[a].append((0, b))
        edgeList[b].append((0, a))
    print(edgeList)
    for a, b, cost in edgesToRepair:
        edgeList[a] = updateCost(edgeList[a], cost, b)
        edgeList[b] = updateCost(edgeList[b], cost, a)
    print(edgeList)
    # find shorted spanning graph
    reached = set()
    totalCost = 0
    pq = queue.PriorityQueue()
    pq.put((0, 1))
    while len(reached) < n:
        current = pq.get()
        currentNode = current[1]
        cost = current[0]
        if currentNode not in reached:
            reached.add(currentNode)
            totalCost += cost
            for neighbor in edgeList[currentNode]:
                pq.put(neighbor)
    return totalCost


n = 6
edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
print(minCostRepair(n, edges, edgesToRepair))
