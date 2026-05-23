# Problem: Unique Morse Code Words
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 7

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mylist=[]
        for i in words:
            temp=""
            for j in i:
                temp+=alpha[(ord(j)-97)]
            mylist.append(temp)
        return len(set(mylist))


