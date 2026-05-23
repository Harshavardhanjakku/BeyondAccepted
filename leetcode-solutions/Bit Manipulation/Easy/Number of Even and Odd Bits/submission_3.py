# Problem: Number of Even and Odd Bits
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 3

class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[0,0]
        index=0
        while n!=0:
            if n%2:
                if index%2:
                    l[1]+=1
                if index%2==0:
                    l[0]+=1
            index+=1
            n=n>>1
        return l
