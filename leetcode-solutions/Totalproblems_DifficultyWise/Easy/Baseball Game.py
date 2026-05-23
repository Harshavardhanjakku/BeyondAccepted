# Baseball Game
# Difficulty: Easy
# Language: python

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        l=[]
        for i in operations:
            if i=="C":
                l.pop()
            elif i=="D":
                l.append(int(l[-1])*2)
            elif i=="+":
                l.append(int(l[-1]+l[-2]))
            else:
                l.append(int(i))
        return sum(l)

