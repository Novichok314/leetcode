from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
    
        ans = []
        q = deque([root])
        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(lvl)
        return ans 
