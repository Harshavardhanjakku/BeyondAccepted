# Build an Array With Stack Operations
# Difficulty: Medium
# Language: python

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        length = target[-1]
        indx=0
        mystack=[]
        for num in range(1,length+1):
            if num == target[indx]:
                mystack.append("Push")
                indx+=1
            else:
                mystack.append("Push")
                mystack.append("Pop")
        return mystack

