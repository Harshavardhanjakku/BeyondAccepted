# Problem: Remove All Adjacent Duplicates In String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 4

class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        append = stack.append
        pop = stack.pop

        for ch in s:
            if stack and stack[-1] == ch:
                pop()
            else:
                append(ch)

        return ''.join(stack)
