# Problem: Container With Most Water
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        maxarea=0
        while left<right:
            width=right-left
            lh=height[left]
            rh=height[right]
            area=width*min(lh,rh)
            maxarea=max(maxarea,area)
            if lh<rh:
                left+=1
            else:
                right-=1
        return maxarea

