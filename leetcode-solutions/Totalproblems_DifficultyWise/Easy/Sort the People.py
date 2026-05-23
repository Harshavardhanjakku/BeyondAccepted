# Sort the People
# Difficulty: Easy
# Language: python

class Solution(object):
    def sortPeople(self, names, heights):
        pairs = list(zip(heights, names))
        pairs.sort(reverse=True)
        return [name for _, name in pairs]
