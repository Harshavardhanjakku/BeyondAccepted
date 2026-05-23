# The Two Sneaky Numbers of Digitville
# Difficulty: Easy
# Language: python

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            dic[i]=1+dic.get(i,0)
        res=[]
        for i in dic :
            if dic[i]==2:
                res.append(i)
            if len(res)==2:
                break
        return res


