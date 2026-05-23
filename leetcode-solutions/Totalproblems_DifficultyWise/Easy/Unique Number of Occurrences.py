# Unique Number of Occurrences
# Difficulty: Easy
# Language: python

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        myset=set(arr)
        occ=set()
        for i in myset:
            c=arr.count(i)
            if c in occ:
                return False
            else:
                occ.add(c)
        return True
