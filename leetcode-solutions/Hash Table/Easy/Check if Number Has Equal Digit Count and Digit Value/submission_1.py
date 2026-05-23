# Problem: Check if Number Has Equal Digit Count and Digit Value
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            if num[i]!= str(num.count(str(i))):
                return False
        return True
        
