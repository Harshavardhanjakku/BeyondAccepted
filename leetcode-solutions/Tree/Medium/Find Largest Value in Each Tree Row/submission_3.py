# Problem: Find Largest Value in Each Tree Row
# Difficulty: Medium
# Topic: Tree
# Language: python3
# Submission: 3

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            size = len(q)
            maxi = float('-inf')
            for _ in range(size):
                node = q.popleft()
                maxi = max(maxi, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxi)
        return res
