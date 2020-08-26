class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            n = self.squareSum(n)
            print("n:", n)
            if n in seen:
                return False
        return True

    def squareSum(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n%10)**2
            n //= 10
        return sum



# test driver
sol = Solution()
num = 2
print("Input:", num)
print("Output:", sol.isHappy(num))
