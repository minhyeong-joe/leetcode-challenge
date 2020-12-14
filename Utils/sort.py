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
def quickSort(arr):
    def partition(arr, left, right):
        pivotIndex = left
        pivot = arr[right]
        print("working on index {} to {}:".format(left, right))

        for i in range(left, right):
            print("i={}: comparing {} and {}".format(i, arr[i], pivot))
            if arr[i] <= pivot:
                arr[pivotIndex], arr[i] = arr[i], arr[pivotIndex]
                pivotIndex += 1
            print("{}, pivotIndex={}".format(arr, pivotIndex))
        arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
        return pivotIndex

    def sort(arr, left, right):
        if left < right:
            pivotIndex = partition(arr, left, right)
            sort(arr, left, pivotIndex-1)
            sort(arr, pivotIndex+1, right)

    sort(arr, 0, len(arr)-1)


# binary search (recursive)
def binarySearch_rec(arr, target, left=0, right=None):
    if right is None:
        right = len(arr)-1
    if left > right:
        return -1
    mid = (left+right)//2
    if arr[mid] == target:
        print("{} == {}".format(arr[mid], target))
        return mid
    elif arr[mid] > target:
        print("{} > {}. will now search in {}".format(
            arr[mid], target, arr[left:mid]))
        return binarySearch_rec(arr, target, left, mid-1)
    else:
        print("{} < {}. will now search in {}".format(
            arr[mid], target, arr[mid+1:right+1]))
        return binarySearch_rec(arr, target, mid+1, right)


# binary search (iterative)
def binarySearch_iter(arr, target):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right) // 2
        if arr[mid] == target:
            print("{} == {}".format(arr[mid], target))
            return mid
        elif arr[mid] > target:
            print("{} > {}. will now search in {}".format(
                arr[mid], target, arr[left:mid]))
            right = mid
        else:
            print("{} < {}. will now search in {}".format(
                arr[mid], target, arr[mid+1:right+1]))
            left = mid+1
    return -1


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

    # quick sort test
    print()
    print("*** Quick Sort ***")
    print("Original Array:", arr)
    arr_copy = list(arr)
    quickSort(arr_copy)
    print("Sorted:", arr_copy)

    # binary search test
    print()
    print("*** Binary Search (Recursive) ***")
    target = 32
    print("Sorted Array: {}, target = {}".format(arr_copy, target))
    index = binarySearch_rec(arr_copy, target)
    if index > 0:
        print("Index of {} = {}".format(target, index))
    else:
        print("{} not found in array".format(target))

    print()
    print("*** Binary Search (Iterative) ***")
    target = 97
    print("Sorted Array: {}, target = {}".format(arr_copy, target))
    index = binarySearch_iter(arr_copy, target)
    if index > 0:
        print("Index of {} = {}".format(target, index))
    else:
        print("{} not found in array".format(target))
