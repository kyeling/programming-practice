class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[int(i==j) for i in range(n)] for j in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    memo[i][j] = 2 + memo[i+1][j-1]
                else:
                    memo[i][j] = max(memo[i][j-1], memo[i+1][j-1], memo[i+1][j])

        return memo[0][n-1]
