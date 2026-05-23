# Defanging an IP Address
# Difficulty: Easy
# Language: python

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")
        
