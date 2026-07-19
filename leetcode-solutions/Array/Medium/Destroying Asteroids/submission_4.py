# Problem: Destroying Asteroids
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        for asteroid in sorted(asteroids):
            if mass < asteroid:
                return False
            mass += asteroid
        return True
