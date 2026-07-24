"""
LeetCode 199
Topic: trees
Difficulty: medium
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(node.val)
        return ans



if __name__ == "__main__":
    solution = Solution()
    print(solution.rightSideView())
