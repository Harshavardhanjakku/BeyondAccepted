# Problem: Top K Frequent Elements
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for i in nums :
            freq[i]=freq.get(i,0)+1
        freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        res=[]
        count=1
        print(freq)
        for i in freq:
            res.append(i[0])
            if count==k:
                break
            count+=1
        return res


        
        
