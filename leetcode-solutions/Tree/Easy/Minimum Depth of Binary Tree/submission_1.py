# Problem: Minimum Depth of Binary Tree
# Difficulty: Easy
# Topic: Tree
# Language: python
# Submission: 1

class Solution(object):
    def minDepth(self,root):
        if not root:
            return 0
        from collections import deque
        q=deque()
        q.append([root])
        count=0
        while q:
            nodes=q.popleft()
            count+=1
            temp=[]
            for node in nodes:
                if not node.left and not node.right:
                    return count
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                q.append(temp)
