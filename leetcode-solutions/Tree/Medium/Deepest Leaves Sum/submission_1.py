# Problem: Deepest Leaves Sum
# Difficulty: Medium
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
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            datalist = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                datalist.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(datalist)
        return sum(res[-1])

                    
