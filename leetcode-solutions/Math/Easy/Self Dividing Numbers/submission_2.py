# Problem: Self Dividing Numbers
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        mylis=[]
        for i in range(left,right+1):
            if '0' not in str(i):
                l=list(map(int,str(i)))
                if all(i%x==0 for x in l ):
                    mylis.append(i)
        return mylis

