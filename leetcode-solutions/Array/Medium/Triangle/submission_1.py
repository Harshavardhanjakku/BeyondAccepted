# Problem: Triangle
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m=len(triangle)
        n=len(triangle[0])
        for i in range(1,m):
            for j in range(i+1):
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==i:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        return min(triangle[m-1])
