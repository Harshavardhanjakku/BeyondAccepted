# Problem: Simplify Path
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        mystack=[]
        d=path.split("/")
        for i in d:
            if i=="." or i=="":
                continue
            elif i==".." :
                if mystack:
                    mystack.pop() 
            else:
                mystack.append(i)
        return "/"+"/".join(mystack)
       

