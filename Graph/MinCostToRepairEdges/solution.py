from collections import defaultdict


def updateCost(neighbors, b, cost):
    for i in range(len(neighbors)):
        if neighbors[i][0] == b:
            neighbors[i][1] = cost


def minCostRepair(n, edges, edgesToRepair):
    # create edge lists associated with cost
    edgeList = defaultdict(list)
    for a, b in edges:
        edgeList[a].append([b, 0])
        edgeList[b].append([a, 0])
    # print(edgeList)
    for a, b, cost in edgesToRepair:
        updateCost(edgeList[a], b, cost)
        updateCost(edgeList[b], a, cost)
    # print(edgeList)
    # find shorted spanning graph
    reached = set()
    totalCost = 0
    queue = list()
    queue.append([1, 0])
    while len(reached) < n:
        current = queue.pop(0)
        currentNode = current[0]
        cost = current[1]
        if currentNode not in reached:
            reached.add(currentNode)
            totalCost += cost
            queue.extend(edgeList[currentNode])
            queue.sort(key=lambda pair: pair[1])
    return totalCost


n = 6
edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
print(minCostRepair(n, edges, edgesToRepair))
