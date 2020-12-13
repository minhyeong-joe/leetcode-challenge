import math


class Solution:
    # brute force, find all permutations and return the k-th permutation (slow, LC submission time limit exceed)
    def getPermutation(self, n: int, k: int) -> str:
        def permute_rec(nums, start):
            if start >= len(nums):
                stringFormat = ""
                for num in nums:
                    stringFormat += str(num)
                allPermutations.append(stringFormat)

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permute_rec(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]

        nums = [n+1 for n in range(n)]
        allPermutations = list()
        permute_rec(nums, 0)
        allPermutations.sort()
        return allPermutations[k-1]

    # smarter way from LC discuss (using mathematics)
    """
    One main thing to consider is that when you have a five digit number possible numbers are 1,2,3,4,5.
    So the number of permutations that start with 1 are (5-1)! = 4!
    Similarly with 2 and 3 and 4 and 5.
    So if the k = 32 it means that i need to cross all the possibilites with 1 which are 24. and then check in the possibilties that start with 2. now we have crossed 24 possibilties so 32-24=8 are remaining.
    Now repeat the whole process with second significant digit.
    """

    def getPermutation_smart(self, n: int, k: int) -> str:
        nums = [n+1 for n in range(n)]
        answer = ""
        while nums:
            fact = len(nums)-1
            numPermEach = math.factorial(fact)
            indexOfNumToAppend = k // numPermEach
            if k % numPermEach == 0:
                indexOfNumToAppend -= 1
            answer += str(nums[indexOfNumToAppend])
            nums.pop(indexOfNumToAppend)
            k -= indexOfNumToAppend * numPermEach
        return answer


sol = Solution()
n = 3
k = 4
print(sol.getPermutation_smart(n, k))
