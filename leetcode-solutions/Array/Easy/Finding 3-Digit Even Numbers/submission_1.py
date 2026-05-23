# Problem: Finding 3-Digit Even Numbers
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        myset = set()
        for perm in itertools.permutations(digits, 3): 
            if perm[0] != 0: 
                if perm[2] % 2 == 0:
                    number = perm[0] * 100 + perm[1] * 10 + perm[2]
                    myset.add(number) 
        return sorted(list(myset))

