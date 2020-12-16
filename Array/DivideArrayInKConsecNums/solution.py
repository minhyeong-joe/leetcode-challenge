from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # if array length is not divisible by k, then there can never be even sets of k intgers
        if len(nums) % k != 0:
            return False
        # sort array
        nums.sort()
        while nums:
            consecutiveSet = list()
            consecutiveSet.append(nums[0])
            for i in range(1, len(nums)+1):
                # if out of bound, then not possible with remaining integers
                if i == len(nums):
                    return False
                # if current number is strictly ONE greater than prev one, add it to consecutive set (to be removed from array)
                if nums[i] == consecutiveSet[-1] + 1:
                    consecutiveSet.append(nums[i])
                elif nums[i] > consecutiveSet[-1] + 1:
                    return False
                # if we found k consecutive integers, remove them from array and repeat
                if len(consecutiveSet) == k:
                    for num in consecutiveSet:
                        nums.remove(num)
                    break
        return True


sol = Solution()
nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3
print(f'Input: nums = {nums}, k = {k}')
print("Output:", sol.isPossibleDivide(nums, k))
