from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        binSum = 0
        mask = bin((1 << 32) - 1)
        uniqueBin = ""
        for num in nums:
            binary = int(bin(num & int(mask, 2))[2:])
            print(num, "=", binary)
            binSum += binary
        print("sum =", binSum)
        for bit in str(binSum):
            if int(bit) % 3 != 0:
                uniqueBin += "1"
            else:
                uniqueBin += "0"
        print("unique number in binary:", uniqueBin)
        if int(uniqueBin, 2) > 2**31:
            uniqueBin = str(bin(int(uniqueBin, 2)-1))
            print(uniqueBin)
            print(bin((~int(uniqueBin, 2) & int(mask, 2))))
            return -(~int(uniqueBin, 2) & int(mask, 2))
        return int(uniqueBin, 2)


# test driver
sol = Solution()
input = [2, 3, 2, 2]
print("Input:", input)
print("Output:", sol.singleNumber(input))
