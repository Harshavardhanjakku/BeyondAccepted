# Problem: Finding 3-Digit Even Numbers
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from itertools import combinations 
        mylist=list(itertools.permutations(digits, 3))
        res=[]
        dic={}
        for i in mylist: 
            if i[0]!=0 :
                temp=100*(i[0])+10*(i[1])+1*(i[2])
                if temp%2==0 and (temp not in dic):
                    res.append(temp)
                    dic[temp]=True
        return sorted(res)

