# Problem: Sort the Students by Their Kth Score
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x:x[k],reverse=True)
