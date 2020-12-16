from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        binSum = 0
        mask = bin((1<<32) -1)
        uniqueBin = ""
        for num in nums:
            binary = int(bin(num & int(mask,2))[2:])
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
            uniqueBin = str(bin(int(uniqueBin,2)-1))
            print(uniqueBin)
            print(bin((~int(uniqueBin, 2) & int(mask,2))))
            return -(~int(uniqueBin, 2) & int(mask,2))
        return int(uniqueBin, 2)
        

# test driver
sol = Solution()
input = [-19,-46,-19,-46,-9,-9,-19,17,17,17,-13,-13,-9,-13,-46,-28]
print("Input:", input)
print("Output:", sol.singleNumber(input))