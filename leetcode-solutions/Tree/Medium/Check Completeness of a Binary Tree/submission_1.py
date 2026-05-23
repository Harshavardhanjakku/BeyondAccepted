# Problem: Check Completeness of a Binary Tree
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 1

from collections import deque

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q = deque()
        q.append(root)
        flag = False
        
        while q:
            node = q.popleft()
            
            if node is None:
                flag = True
            else:
                if flag:
                    return False
                q.append(node.left)
                q.append(node.right)
        
        return True

