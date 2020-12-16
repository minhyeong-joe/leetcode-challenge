class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for c in range(len(p)+1)] for c in range(len(s)+1)]
        dp[-1][-1] = True
        for j in range(len(p)-1, -1, -1):
            if j+1 < len(p) and p[j+1] == "*":
                dp[-1][j] = dp[-1][j+2]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                if p[j] == "*":
                    continue
                isMatching = p[j] == s[i] or p[j] == "."
                if j+1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (isMatching and dp[i+1][j])
                else:
                    dp[i][j] = isMatching and dp[i+1][j+1]
        return dp[0][0]


sol = Solution()
s = "aaa"
p = "ab*a"
print(sol.isMatch(s, p))

s = "aab"
p = "c*a*b"
print(sol.isMatch(s, p))

s = "mississippi"
p = "mis*is*p*."
print(sol.isMatch(s, p))
