# Problem: Majority Element II
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        ol=[]
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            if dic[i]>n//3:
                ol.append(i)
        return ol
        
