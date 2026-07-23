from topics.trees.easy.problem_94 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.inorderTraversal(None) == []
    assert solution.inorderTraversal(TreeNode(1)) == [1]
    assert solution.inorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3))) == [2, 1, 3]