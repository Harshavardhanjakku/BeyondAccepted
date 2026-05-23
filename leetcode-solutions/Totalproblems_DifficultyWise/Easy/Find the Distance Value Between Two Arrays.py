# Find the Distance Value Between Two Arrays
# Difficulty: Easy
# Language: python

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n=len(arr2)
        arr2.sort()
        def binarysearch(num):
            low=0
            high=n-1
            while low<=high:
                mid=low+(high-low)//2
                if arr2[mid]<num-d:
                    low= mid + 1
                elif arr2[mid]>num+d:
                    high= mid-1
                else:
                    return True
            return False
        count=0
        for i in arr1:
            if not binarysearch(i):
                count+=1
        return count
