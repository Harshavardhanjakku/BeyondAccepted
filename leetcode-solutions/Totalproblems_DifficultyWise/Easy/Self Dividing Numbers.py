# Self Dividing Numbers
# Difficulty: Easy
# Language: python

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            temp = num = i 
            flag=True 
            while temp>0:
                r=temp%10
                if r==0 or num%r!=0:
                    flag=False
                    break
                temp//=10
            if flag :
                res.append(num)
        return res

            
