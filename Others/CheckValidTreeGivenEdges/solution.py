def isValidEdges(n, edges):
    connected = set()
    for a, b in edges:
        if a in connected and b in connected:
            return False
        connected.add(a)
        connected.add(b)
    return True


n = 4
edges = [(0, 1), (2, 0), (3, 2)]
print(isValidEdges(n, edges))

edges = [(0, 1), (0, 2), (2, 1), (0, 3)]
print(isValidEdges(n, edges))
