# Problem: Reverse String Prefix
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 2

class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res=list(s)
        def rev(start,end):
            while start<end:
                res[start],res[end]=res[end],res[start]
                start+=1
                end-=1
        rev(0,k-1)
        return "".join(res)

