# Problem: Evaluate Reverse Polish Notation
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for tok in tokens:
            if tok in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(float(a) / b))  
            else:
                stack.append(int(tok))

        return stack[0]

