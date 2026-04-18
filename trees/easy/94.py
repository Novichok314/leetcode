class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []
        def ord(root):
            if not root:
                return 
            
            ord(root.left)
            ans.append(root.val)
            ord(root.right)
        ord(root)
        return ans