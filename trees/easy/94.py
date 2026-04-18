class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root: return []
        ans = []
        def ord(root):
            if not root.left and not root.right:
                ans.append(root.val)
                return 
            if root.left: ord(root.left)
            ans.append(root.val)
            if root.right: ord(root.right)
        ord(root)
        return ans