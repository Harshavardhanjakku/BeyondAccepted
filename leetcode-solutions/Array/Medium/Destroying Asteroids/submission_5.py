# Problem: Destroying Asteroids
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for asteroid in asteroids :
            if mass<asteroid :
                return False
            mass+=asteroid
        return True
