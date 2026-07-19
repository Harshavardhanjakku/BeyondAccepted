# Problem: Restore Finishing Order
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        d={}
        for f in friends :
            d[f]=True
        return [o for o in order if o in d ]
