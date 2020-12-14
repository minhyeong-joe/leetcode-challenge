import random
import heapq

# insertion sort


def insertionSort(arr):
    for i in range(1, len(arr)):
        print("Run {0}:".format(i))
        print(arr)
        for j in range(i):
            if arr[i-j] < arr[i-j-1]:
                arr[i-j], arr[i-j-1] = arr[i-j-1], arr[i-j]
                print(arr)

# bubble sort


def bubbleSort(arr):
    for i in range(len(arr)-1):
        print("Run {0}:".format(i+1))
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

# heap sort


def heapSort(arr):
    heap = list(arr)
    heapq.heapify(heap)
    print("Heapified Array:", heap)
    arr.clear()
    while heap:
        arr.append(heapq.heappop(heap))
        print("Add min from heap:", arr)
        print("Heapified Array:", heap)


# merge sort

def mergeSort(arr):
    # helper recursion to divide into subproblems
    def divideAndConquer(arr, left=0, right=None):
        if right is None:
            right = len(arr)-1
        if left >= right:
            return
        mid = (left+right) // 2
        divideAndConquer(arr, left, mid)
        divideAndConquer(arr, mid+1, right)
        merge(arr, left, mid, right)

    # merge subproblems and compare as merging
    def merge(arr, left, mid, right):
        tempArray = [None]*(len(arr))
        left1 = left
        right1 = mid
        left2 = mid+1
        right2 = right
        temp_index = left
        while left1 <= right1 and left2 <= right2:
            if arr[left1] <= arr[left2]:
                tempArray[temp_index] = arr[left1]
                left1 += 1
            else:
                tempArray[temp_index] = arr[left2]
                left2 += 1
            temp_index += 1
        while left1 <= right1:
            tempArray[temp_index] = arr[left1]
            left1 += 1
            temp_index += 1
        while left2 <= right2:
            tempArray[temp_index] = arr[left2]
            left2 += 1
            temp_index += 1
        print("Temporary Array:", tempArray)
        for i in range(left, right+1):
            arr[i] = tempArray[i]
        print("Actual Array:   ", arr)

    divideAndConquer(arr)


# quick sort

# binary search (recursive)
# binary search (iterative)
if __name__ == "__main__":
    # generate random array
    arr = list()
    random.seed(1)
    for i in range(10):
        arr.append(random.randint(0, 100))
    print("random array:", arr)

    # insertion sort test
    print()
    print("*** Insertion Sort ***")
    print("Original Array:", arr)
    arr_copy = list(arr)
    insertionSort(arr_copy)
    print("sorted:", arr_copy)

    # bubble sort test
    print()
    print("*** Bubble Sort ***")
    print("Original Array:", arr)
    arr_copy = list(arr)
    bubbleSort(arr_copy)
    print("Sorted:", arr_copy)

    # heap sort test
    print()
    print("*** Heap Sort ***")
    print("Original Array:", arr)
    arr_copy = list(arr)
    heapSort(arr_copy)
    print("Sorted:", arr_copy)

    # merge sort test
    print()
    print("*** Merge Sort ***")
    print("Original Array:", arr)
    arr_copy = list(arr)
    mergeSort(arr_copy)
    print("Sorted:", arr_copy)
