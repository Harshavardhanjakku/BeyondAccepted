# Problem: Ransom Note
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
