SOURCE = 'S'
DANGER = 'D'
TREASURE = 'X'


def shortestRoute(map):
    routes = set()

    def dfs(map, currentRow, currentCol, visited=list()):
        # check for out of bound or dangerous or visited
        if currentRow < 0 or currentRow >= len(map) or currentCol < 0 or currentCol >= len(map[currentRow]) or map[currentRow][currentCol] == DANGER or (currentRow, currentCol) in visited:
            return
        if map[currentRow][currentCol] == TREASURE:
            # optional print route for debugging (if not used, visited can be set() instead of list() for a tiny performance improvement)
            route = [v for v in visited]
            route.append((currentRow, currentCol))
            print("Route:", route)
            routes.add(len(visited))
            return
        # navigate
        # print(f'{map[currentRow][currentCol]} ({currentRow}, {currentCol})')
        visited.append((currentRow, currentCol))
        dfs(map, currentRow-1, currentCol, visited)  # up
        dfs(map, currentRow, currentCol+1, visited)  # right
        dfs(map, currentRow+1, currentCol, visited)  # down
        dfs(map, currentRow, currentCol-1, visited)  # left
        visited.remove((currentRow, currentCol))

    for i, row in enumerate(map):
        for j, mark in enumerate(row):
            if mark == SOURCE:
                dfs(map, i, j)
    return min(routes) if routes else None


map = [['S', 'O', 'O', 'S', 'S'],
       ['D', 'O', 'D', 'O', 'D'],
       ['O', 'O', 'O', 'O', 'X'],
       ['X', 'D', 'D', 'O', 'O'],
       ['X', 'D', 'D', 'D', 'O']]

print(shortestRoute(map))
