from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = list()
        # insert newInterval sorted by start time
        insertIndex = 0
        for i, interval in enumerate(intervals):
            if newInterval[0] >= interval[0]:
                insertIndex = i+1
        intervals.insert(insertIndex, newInterval)
        print(intervals)
        # use queue to merge from low start time
        while intervals:
            cur = intervals.pop(0)
            if not result:
                result.append(cur)
                continue
            if result[-1][0] <= cur[0] <= result[-1][1]:
                start = result[-1][0]
                end = max(result[-1][1], cur[1])
                result[-1] = [start, end]
            else:
                result.append(cur)
        return result


# test driver
sol = Solution()
intervals = [[2,3], [6,8]]
newInterval = [4,7]
print("Output:", sol.insert(intervals, newInterval))