class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        max_val = float('inf')
        min_val = float('-inf')
        def validate(node: TreeNode, min_val, max_val) -> bool:
            if not node: return True
            return min_val < node.val < max_val and validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        return validate(root, min_val, max_val)


