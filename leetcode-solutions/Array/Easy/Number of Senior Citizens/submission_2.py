# Problem: Number of Senior Citizens
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for i in details:
            if int(i[-4:-2])>60:
                count+=1
        return count
        
