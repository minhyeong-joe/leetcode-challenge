class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        # print(arr)
        for i, n in enumerate(arr):
            n = int(n)
            maxNum = max([int(num) for num in arr[i:]])
            if maxNum > n:
                for j in range(len(arr)-1, i-1, -1):
                    if int(arr[j]) == maxNum:
                        arr[i], arr[j] = arr[j], arr[i]
                        # print(arr)
                        return int("".join(arr))
        return int("".join(arr))



# test driver
sol = Solution()
num = 2736
print("Input:", num)
print("Output:", sol.maximumSwap(num))

num = 98368
print("Input:", num)
print("Output:", sol.maximumSwap(num))