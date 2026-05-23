# Problem: Group Anagrams
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for i in strs:
            t="".join(sorted(i))
            if t not in dic:
                dic[t]=[i]
            else:
                dic[t]+=[i]
        return dic.values()
