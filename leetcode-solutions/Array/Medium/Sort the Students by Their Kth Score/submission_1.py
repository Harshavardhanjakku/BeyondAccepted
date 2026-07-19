# Problem: Sort the Students by Their Kth Score
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: x[k], reverse=True)

        return score
