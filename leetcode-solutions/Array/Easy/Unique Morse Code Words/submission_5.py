# Problem: Unique Morse Code Words
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        myset=set()
        for i in words:
            temp=""
            for j in i:
                temp+=alpha[(ord(j)-97)]
            myset.add(temp)
        return len(myset)


