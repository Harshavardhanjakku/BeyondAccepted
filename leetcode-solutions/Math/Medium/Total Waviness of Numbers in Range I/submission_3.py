# Problem: Total Waviness of Numbers in Range I
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        tot=0
        for num in range(num1,num2+1):
            l=list(map(int,list(str(num))))
            n=len(l)
            waviness=0
            for i in range(1,n-1):
                if l[i-1]>l[i]<l[i+1] or l[i-1]<l[i]>l[i+1]:
                    waviness+=1
            tot+=waviness
        return tot

