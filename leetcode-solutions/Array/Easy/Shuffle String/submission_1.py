# Problem: Shuffle String
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        l=list(s)
        for idx,val in enumerate(indices):
            ch=s[idx]
            l[val]=ch
        return "".join(l)
