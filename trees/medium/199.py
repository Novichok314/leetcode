from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root: return []

        q = deque([root])
        ans = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(node.val)
        return ans 