from topics.trees.easy.problem_104 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.maxDepth(None) == 0
    assert solution.maxDepth(TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(3))))
