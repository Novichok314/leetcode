from topics.trees.medium.problem_103 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.zigzagLevelOrder(None) == []
    assert solution.zigzagLevelOrder(TreeNode(1)) == [[1]]
    assert solution.zigzagLevelOrder(TreeNode(1, TreeNode(2), TreeNode(3))) == [[1], [3, 2]]
    