# Problem: Robot Return to Origin
# Difficulty: Easy
# Topic: String
# Language: python3
# Submission: 1

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
