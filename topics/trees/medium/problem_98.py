"""
LeetCode 98
Topic: trees
Difficulty: medium
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = float('-inf')
        max_val = float('inf')
        def validate(node, min_val, max_val):
            if not node:
                return True
            return min_val < node.val < max_val and \
                     validate(node.left, min_val, node.val) and \
                     validate(node.right, node.val, max_val)
        return validate(root, min_val, max_val)

        


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidBST())
