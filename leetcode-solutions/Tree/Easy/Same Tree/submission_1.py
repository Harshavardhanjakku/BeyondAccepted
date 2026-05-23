# Problem: Same Tree
# Difficulty: Easy
# Topic: Tree
# Language: python
# Submission: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        from collections import deque
        queue= deque()
        queue.append((p,q))
        while queue:
            n1,n2=queue.popleft()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            elif n1.val!=n2.val:
                return False
            queue.append((n1.left,n2.left))
            queue.append((n1.right,n2.right))
        return True
            
