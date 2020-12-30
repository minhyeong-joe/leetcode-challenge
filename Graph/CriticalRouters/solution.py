from collections import defaultdict


def criticalRouters(numNodes, numEdges, edges):
    criticalVertices = list()
    adjList = defaultdict(list)
    # convert edges array form into adjacency list
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    # print(adjList)
    for source, destinations in adjList.items():
        if len(destinations) <= 1:
            continue
        firstDest = destinations[0]
        for dest in destinations[1:]:
            if not reachable(adjList, firstDest, dest, source):
                criticalVertices.append(source)
                break

    return criticalVertices

# use BFS to see if 'src' can reach 'dest' without going through 'blockedVertex'
# if false, that means 'blockedVertex' is a critical vertex


def reachable(adjList, src, dest, blockedVertex):
    queue = list()
    visited = set()
    visited.add(blockedVertex)
    queue.append(src)
    while queue:
        current = queue.pop(0)
        if current == dest:
            return True
        visited.add(current)
        for neighbor in adjList[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False


numNodes = 7
numEdges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
print(criticalRouters(numNodes, numEdges, edges))
