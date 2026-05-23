# Problem: Defanging an IP Address
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        add=address.split(".")
        return "[.]".join(add)
        
