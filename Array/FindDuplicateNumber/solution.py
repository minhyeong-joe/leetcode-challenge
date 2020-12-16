from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[nums[0]]
        hare = nums[tortoise]
        print("tortoise: {}, hare: {}".format(tortoise, hare))
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            print("tortoise: {}, hare: {}".format(tortoise, hare))
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            print("tortoise: {}, hare: {}".format(tortoise, hare))
        return tortoise


# [1,3,4,2,2] equivalent to
# idx 0 (1) -> idx 1 (3) -> idx 3 (2) -> idx 2 (4) -> idx 4 (2) -> idx 2 (4) ... cycle
#
sol = Solution()
nums = [1, 3, 4, 2, 2]
print(sol.findDuplicate(nums))
