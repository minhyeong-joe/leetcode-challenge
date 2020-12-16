
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longestLength = 0
        left = 0
        right = 0
        # create N x N dynamic programming table and init with setting i==j true
        # because a word of length 1 is always palindromic
        dp = [[False for n in range(N)] for n in range(N)]
        for i in range(N):
            dp[i][i] = True
        # print(dp)
        # bottom-up fill-in
        # if length of 2 -> palindromic iff two letters are same
        # if longer length -> palindromic iff start and end letters are same AND
        #                     inner word is palindromic (check for [i+1][j-1])
        for i in range(N-2, -1, -1):
            for j in range(N-1, i-1, -1):
                if i == j-1:
                    if s[i] == s[j]:
                        dp[i][j] = s[i] == s[j]
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j]:
                    if j-i+1 > longestLength:
                        # new longest palindromic substring, so update
                        longestLength = j-i+1
                        left = i
                        right = j
                    break
        print(dp)
        return s[left:right+1]


sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))
