# Problem: Three Consecutive Odds
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        for i in range(0,n-2):
            if all([arr[i]%2,arr[i+1]%2,arr[i+2]%2]):
                return True
        return False
        
