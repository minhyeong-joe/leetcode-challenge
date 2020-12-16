from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotations repeat in modulo
        # k %= len(nums)
        i = 0
        count = 0
        while count < len(nums):
            start = i
            copy = nums[i]
            while True:
                j = (i + k) % len(nums)  # allows end of array "cycle" back to beginning of array
                copy, nums[j] = nums[j], copy
                i = j
                count += 1
                if i == start:
                    break
            i += 1



# test driver
sol = Solution()
nums = [1,2]
k = 3
sol.rotate(nums, k)
print("Output:", nums)