# Problem: Binary Tree Right Side View
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import deque
        q=deque()
        q.append([root])
        if not root:
            return []
        res=[root.val]
        while q :
            nodelist=q.popleft()
            temp=[]
            for node in nodelist :
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                res.append(temp[-1].val)
                q.append(temp)
        return res



