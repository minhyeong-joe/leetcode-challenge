from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = defaultdict(list)
        for departure, destination in sorted(tickets, reverse=True):
            destinations[departure] += destination,
        print(destinations)
        route = []

        def visit(airport):
            while destinations[airport]:
                visit(destinations[airport].pop())
            route.append(airport)

        visit('JFK')
        route.reverse()
        return route


sol = Solution()
tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print(sol.findItinerary(tickets))
