# Problem: Unique Paths
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n for _ in range(m)]

        def myfun(i, j):
            if i == m-1 and j == n-1:
                dp[i][j] = 1
                return dp[i][j]
            if i >= m or j >= n:
                return 0
            if dp[i][j]:
                return dp[i][j]
            dp[i][j] = myfun(i+1, j) + myfun(i, j+1)
            return dp[i][j]

        startrow, startcol = 0, 0
        myfun(startrow, startcol)
        print(dp)
        return dp[0][0]

