# Number of Students Doing Homework at a Given Time
# Difficulty: Easy
# Language: python

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        n=len(startTime)
        count=0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                count+=1
        return count
