# Problem: Minimum Time to Make Rope Colorful
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        n=len(colors)
        time=0 
        for i in range(n-1):
            if colors[i]==colors[i+1]:
                if neededTime[i]>neededTime[i+1]:
                    time+=neededTime[i+1]
                    neededTime[i+1]=neededTime[i]
                else:
                    time+=neededTime[i]
        return time


