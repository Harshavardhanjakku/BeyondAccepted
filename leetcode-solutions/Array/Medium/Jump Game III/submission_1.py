# Problem: Jump Game III
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n=len(arr)
        dp=[-1]*n
        def jump(idx):
            if idx<0 or idx>=n :
                return False
            if arr[idx]==0:
                dp[idx]=True
                return True 
            if dp[idx]!=-1:
                return dp[idx]
            dp[idx]=False
            dp[idx]=jump(idx-arr[idx]) or jump(idx+arr[idx]) 
            return dp[idx]
        return jump(start)
