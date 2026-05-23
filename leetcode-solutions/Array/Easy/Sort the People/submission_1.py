# Problem: Sort the People
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def sortPeople(self, names, heights):
        pairs = list(zip(heights, names))
        pairs.sort(reverse=True)
        return [name for _, name in pairs]
