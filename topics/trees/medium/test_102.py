from topics.trees.easy.problem_101 import TreeNode
from topics.trees.medium.problem_102 import Solution


def test():
    solution = Solution()
    assert solution.levelOrder(None) == []
    assert solution.levelOrder(TreeNode(1)) == [[1]]
    assert solution.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3))) == [[1], [2, 3]]
