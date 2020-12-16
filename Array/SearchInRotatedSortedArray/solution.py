from typing import List

def search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)-1
    while end >= start:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[start]:
            # mid belongs to left sorted subarray
            if target < nums[mid] and target >= nums[start]:
                # target is in left subarray
                end = mid - 1
            elif target < nums[mid] and target < nums[start]:
                # target is in right subarray
                start = mid + 1
            elif target > nums[mid]:
                # target is in right subarray
                start = mid + 1
        else:
            # mid belongs to right sorted subarray
            if target < nums[mid]:
                # target is in left subarray
                end = mid - 1
            elif target > nums[mid] and target <= nums[end]:
                # target is in right subarray
                start = mid + 1
            elif target > nums[mid] and target > nums[end]:
                # target is in left subarray
                end = mid - 1
    return -1
        



# test driver
nums = [4,5,6,7,0,1,2]
target = 0
print("Input: nums =", nums, ", target =", target)
print("Output:", search(nums, target))
print()

nums = [6,7,0,1,2,4,5]
target = 0
print("Input: nums =", nums, ", target =", target)
print("Output:", search(nums, target))
print()