from typing import List
from collections import defaultdict, deque

# this method does not work if there's cyclic dependency (ie. a course A with prereq B that has prereq A)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        availableCourses = defaultdict(list)
        for course, prereq in prerequisites:
            availableCourses[course].append(prereq)

        def takeCourse(course):
            if not availableCourses[course]:
                if course not in courses:
                    courses.append(course)
                return

            for c in availableCourses[course]:
                takeCourse(c)
            if course not in courses:
                courses.append(course)

        courses = list()
        for i in range(0, numCourses):
            takeCourse(i)
        return courses


sol = Solution()
numCourses = 6
prereq = [[1, 0], [2, 0], [3, 1], [3, 2], [3, 5]]
print(sol.findOrder(numCourses, prereq))
