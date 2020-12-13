from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        topological_list = list()
        queue = list()
        # associate indegree and prereq for each courses
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        print(graph)
        # start by adding all courses from 0 that have indegree of 0
        for i in range(numCourses):
            # add all the courses with indegree of 0
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            print("Indegree:", indegree)
            print("Queue:", queue)
            currentCourse = queue.pop(0)
            topological_list.append(currentCourse)
            # for each course that needs currentCourse as prereq, decrement indegree by 1 (since currentCourse is "completed"), when indegree of course == 0, then add to queue to be added in topological order
            for course in graph[currentCourse]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return topological_list if len(topological_list) == numCourses else []


sol = Solution()
numCourses = 3
prereq = [[1, 0], [1, 2], [0, 1]]
print(sol.findOrder(numCourses, prereq))
