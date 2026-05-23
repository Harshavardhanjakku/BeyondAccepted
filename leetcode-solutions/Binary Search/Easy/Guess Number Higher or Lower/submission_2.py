# Problem: Guess Number Higher or Lower
# Difficulty: Easy
# Topic: Binary Search
# Language: python
# Submission: 2

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        while low<=high:
            mid=low+(high-low)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res==1:
                low=mid+1
            else:
                high=mid-1
                

