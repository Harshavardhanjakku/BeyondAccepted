# Problem: Goal Parser Interpretation
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command=command.replace("()","o")
        command=command.replace("(al)","al")
        return command

