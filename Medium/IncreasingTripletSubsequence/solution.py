from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False
    lowest = None
    mid = None
    for i in range(0, len(nums)):
        # compare if current value is greater than mid
        if mid is not None and nums[i] > mid:
            return True
        # assign mid
        if lowest is not None and lowest < nums[i]:
            if mid is None or mid > nums[i]:
                mid = nums[i]
        # assign lowest
        if lowest is None or lowest > nums[i]:
            lowest = nums[i]
    return False
                    
        

# test driver
input = [1, 2, 3, 4, 5]
print("Input:", input)
print("Output:", increasingTriplet(input))

input = [2, 5, 3, 4, 5]
print("Input:", input)
print("Output:", increasingTriplet(input))

input = [5, 4, 3, 2, 1]
print("Input:", input)
print("Output:", increasingTriplet(input))
