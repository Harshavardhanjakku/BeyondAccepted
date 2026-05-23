# Problem: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            elif s < target:
                i += 1
            else:
                j -= 1

