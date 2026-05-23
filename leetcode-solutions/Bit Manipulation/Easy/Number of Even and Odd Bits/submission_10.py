# Problem: Number of Even and Odd Bits
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 10

class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        oc=0
        ec=0
        index=0
        while n!=0:
            if n&1 and index&1:
                oc+=1
            elif n&1 and index&1==0:
                ec+=1
            index+=1
            n=n>>1
        return [ec,oc]
