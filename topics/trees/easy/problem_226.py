"""
LeetCode 226
Topic: trees
Difficulty: easy
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))


if __name__ == "__main__":
    solution = Solution()
    print(solution.invertTree())
