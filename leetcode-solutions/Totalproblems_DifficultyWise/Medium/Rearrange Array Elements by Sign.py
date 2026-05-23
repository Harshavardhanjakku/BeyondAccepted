# Rearrange Array Elements by Sign
# Difficulty: Medium
# Language: python

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pl=[x for x in nums if x>0]
        nl=[x for x in nums if x<0]
        res=[]
        for i in range(len(pl)):
            res.append(pl[i])
            res.append(nl[i])
        return res

