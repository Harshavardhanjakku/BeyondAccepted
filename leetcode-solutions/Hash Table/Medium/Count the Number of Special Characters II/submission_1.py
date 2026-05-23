# Problem: Count the Number of Special Characters II
# Difficulty: Medium
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def numberOfSpecialChars(self, word):
        dic = {}
        for idx, value in enumerate(word):
            if value.islower():
                if value not in dic:
                    dic[value] = [idx, float('inf')]
                else:
                    dic[value][0] = idx
            else:
                low = value.lower()
                if low not in dic:
                    dic[low] = [-1, idx]
                else:
                    if dic[low][1] == float('inf'):
                        dic[low][1] = idx
        count = 0
        for key in dic:
            if dic[key][0] != -1 and dic[key][1] != float('inf') and dic[key][0] < dic[key][1]:
                count += 1
        return count

