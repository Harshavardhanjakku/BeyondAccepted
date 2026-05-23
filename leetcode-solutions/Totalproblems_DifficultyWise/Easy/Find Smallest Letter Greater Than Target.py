# Find Smallest Letter Greater Than Target
# Difficulty: Easy
# Language: python

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low=0
        high=len(letters)-1
        res=-1
        while low<=high:
            mid=low+(high-low)//2
            if target<letters[mid]:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return letters[res] if res!=-1 else letters[0]


