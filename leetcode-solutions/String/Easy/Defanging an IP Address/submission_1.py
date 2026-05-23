# Problem: Defanging an IP Address
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")
        
