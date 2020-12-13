from typing import List
from collections import defaultdict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute_rec(freqDict: defaultdict, permutation: List[int]):
            remSum = 0
            for count in freqDict.values():
                remSum += count
            if remSum <= 0:
                result.append(list(permutation))
                return

            for num, count in freqDict.items():
                if count > 0:
                    freqDict[num] -= 1
                    permutation.append(num)
                    permute_rec(freqDict, permutation)
                    permutation.pop()
                    freqDict[num] += 1

        result = list()
        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] += 1
        print(freqDict)
        permute_rec(freqDict, [])
        return result


sol = Solution()
nums = [1, 1, 2]
print(sol.permuteUnique(nums))
