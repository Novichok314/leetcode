"""
LeetCode 94
Topic: trees
Difficulty: easy
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.inorderTraversal())
