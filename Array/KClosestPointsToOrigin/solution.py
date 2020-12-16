from typing import List


class MaxHeap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify()

    def getMax(self):
        return self.heap[0]

    def popMax(self):
        maxVal = self.heap.pop(0)
        self.heapify()

    def size(self):
        return len(self.heap)

    def heapify(self):
        for i in range(len(self.heap)-1, 0, -1):
            parentIndex = (i-1) // 2
            if self.heap[i][0] > self.heap[parentIndex][0]:
                self.heap[i], self.heap[parentIndex] = self.heap[parentIndex], self.heap[i]

    def __str__(self):
        return str(self.heap)

    def __iter__(self):
        return (x for x in self.heap)


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        closest = list(list())
        # find Euclidean distance and put them in key value pair
        distances = []
        for point in points:
            squareSum = point[0]**2 + point[1]**2
            distances.append((squareSum, point))
        print(distances)
        # use max heap of size K to only hold K closest pairs
        maxHeap = MaxHeap()
        for distance, point in distances:
            # print(distance, point)
            # if maxheap has space, then insert
            if maxHeap.size() < K:
                maxHeap.insert((distance, point))
            else:
                if distance < maxHeap.getMax()[0]:
                    maxHeap.popMax()
                    maxHeap.insert((distance, point))
        # return all K pairs in max heap
        print([pair[1] for pair in maxHeap])
        closest.extend([pair[1] for pair in maxHeap])
        return closest


sol = Solution()
points = [[3, 3], [5, -1], [-2, 4], [3, 4], [1, 5], [-2, -5], [0, 8]]
K = 4
print(sol.kClosest(points, K))
