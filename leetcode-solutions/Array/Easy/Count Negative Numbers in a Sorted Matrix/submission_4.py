# Problem: Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 4

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            for j in i[::-1]:
                if j>=0:
                    break
                else:
                    count+=1
        return count

