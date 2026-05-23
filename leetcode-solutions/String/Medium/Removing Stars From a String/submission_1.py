# Problem: Removing Stars From a String
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return s
        else:
            mylist=[]
            for i in s:
                if i!="*":
                    mylist.append(i)
                else:
                    mylist.pop()
            return "".join(mylist)
    

