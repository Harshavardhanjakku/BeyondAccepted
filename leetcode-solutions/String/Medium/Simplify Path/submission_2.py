# Problem: Simplify Path
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        mystack=[]
        for i in path.split("/"):
            if i=="." or i=="":
                continue
            elif i==".." :
                if mystack:
                    mystack.pop() 
            else:
                mystack.append(i)
        return "/"+"/".join(mystack)
       

