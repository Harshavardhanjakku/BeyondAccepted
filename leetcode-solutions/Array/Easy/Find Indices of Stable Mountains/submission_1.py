# Problem: Find Indices of Stable Mountains
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def stableMountains(self, height, threshold):
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]
