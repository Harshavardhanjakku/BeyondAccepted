# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left = 0
        maxlen = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= left:
                left = dic[s[i]] + 1
            dic[s[i]] = i
            maxlen = max(maxlen, i - left + 1)

        return maxlen

