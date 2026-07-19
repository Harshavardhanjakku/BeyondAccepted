# Problem: Robot Return to Origin
# Difficulty: Easy
# Topic: String
# Language: python3
# Submission: 3

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        uc=0
        dc=0
        lc=0
        rc=0
        for move in moves :
            if move == "L":
                lc+=1
            elif move == "R":
                rc+=1
            elif move == "U":
                uc+=1
            else:
                dc+=1
        return (lc == rc) and (uc==dc)
