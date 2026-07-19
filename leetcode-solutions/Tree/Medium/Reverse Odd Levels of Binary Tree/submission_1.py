# Problem: Reverse Odd Levels of Binary Tree
# Difficulty: Medium
# Topic: Tree
# Language: python3
# Submission: 1

from collections import deque

class Solution:
    def reverseOddLevels(self, root):
        q = deque([[root]])
        flag = False
        while q:
            nodes = q.popleft()
            temp = []
            if flag:
                vals = [node.val for node in nodes]
                vals.reverse()
                for i in range(len(nodes)):
                    nodes[i].val = vals[i]
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                q.append(temp)
            flag = not flag
        return root
