from typing import List

"""
4 =>    0100
14 =>   1110
2 =>    0010

total hamming distance = sum of hamming distance of every bit
hamming distnace of each bit = num of zeros * num of ones (all pairing differences)
"""
def totalHammingDistance(nums: List[int]) -> int:
    if not nums:
        return 0
    total = 0
    maxBits = len(bin(max(nums))[2:])
    inBinary = [bin(num)[2:].zfill(maxBits) for num in nums]
    for j in range(maxBits):
        numZeros = 0
        for i in range(len(inBinary)):
            numZeros += 1 if inBinary[i][j] == '0' else 0
        total += numZeros * (len(inBinary)-numZeros)
    return total


# test driver
input = [4,14,2]
print("Input:", input)
print("Output:", totalHammingDistance(input))