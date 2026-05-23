# Count Operations to Obtain Zero
# Difficulty: Easy
# Language: python

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count=0
        while(num1!=0 and num2!=0):
            count+=1
            if num1<num2:
                num2=num2-num1
            elif num1 > num2:
                num1=num1-num2
            else:
                break
        else:
            return count  
        return count
