# Problem: Self Dividing Numbers
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(no,x):
            if no%x!= 0:
                return False
            else:
                return True
        mylis=[]
        for i in range(left,right+1):
            if '0' not in str(i):
                l=list(map(int,str(i)))
                if all(check(i,x) for x in l ):
                    mylis.append(i)
        return mylis

