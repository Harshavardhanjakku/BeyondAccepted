# Problem: Guess Number Higher or Lower
# Difficulty: Easy
# Topic: Binary Search
# Language: python
# Submission: 1

class Solution(object):
    def guessNumber(self, n):
        low,high=1,n
        while low <=high:
            mid=(low +high)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res<0:
                high=mid-1
            else:
                low=mid+1
